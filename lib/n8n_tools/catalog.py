"""Generate catalog of n8n workflows with descriptions."""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List
from collections import defaultdict

import click
from rich.console import Console
from rich.progress import track

console = Console(legacy_windows=False, force_terminal=True)


class WorkflowCatalog:
    """Creates a catalog of n8n workflows."""

    def __init__(self):
        self.workflows = []

    def extract_workflow_info(self, workflow_path: Path) -> Dict[str, Any]:
        """Extract information from a workflow file.

        Args:
            workflow_path: Path to the workflow JSON file

        Returns:
            Dictionary with workflow information
        """
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extract basic info
            name = data.get('name', 'Unnamed Workflow')
            nodes = data.get('nodes', [])
            connections = data.get('connections', {})

            # Get workflow metadata
            meta = data.get('meta', {})
            tags = data.get('tags', [])

            # Count node types
            node_types = defaultdict(int)
            trigger_types = []
            integration_nodes = []

            for node in nodes:
                node_type = node.get('type', '')
                node_types[node_type] += 1

                # Identify triggers
                if 'trigger' in node_type.lower():
                    trigger_types.append(node.get('name', node_type))

                # Identify integrations (services)
                if node_type.startswith('n8n-nodes-base.'):
                    service = node_type.replace('n8n-nodes-base.', '')
                    if service not in ['set', 'if', 'merge', 'code', 'function', 'switch']:
                        integration_nodes.append(service)

            # Get category from path
            category = workflow_path.parent.parent.name
            subcategory = workflow_path.parent.name

            return {
                'name': name,
                'path': str(workflow_path),
                'category': category,
                'subcategory': subcategory,
                'node_count': len(nodes),
                'connection_count': len(connections),
                'triggers': list(set(trigger_types)),
                'integrations': list(set(integration_nodes)),
                'tags': [tag.get('name') if isinstance(tag, dict) else str(tag) for tag in tags],
                'has_webhook': any('webhook' in nt.lower() for nt in node_types.keys()),
                'has_schedule': any('schedule' in nt.lower() or 'cron' in nt.lower() for nt in node_types.keys()),
                'has_manual': any('manual' in nt.lower() for nt in node_types.keys()),
            }
        except Exception as e:
            return {
                'name': workflow_path.stem,
                'path': str(workflow_path),
                'error': str(e),
                'category': workflow_path.parent.parent.name,
                'subcategory': workflow_path.parent.name,
            }

    def scan_workflows(self, root_path: Path) -> List[Dict[str, Any]]:
        """Scan directory for workflows.

        Args:
            root_path: Root directory to scan

        Returns:
            List of workflow information dictionaries
        """
        workflow_files = list(root_path.rglob("workflow.json"))

        # Filter out non-workflow JSON files
        workflow_files = [
            f for f in workflow_files
            if not any(skip in str(f) for skip in ['node_modules', '.git', 'lib'])
        ]

        console.print(f"[cyan]Found {len(workflow_files)} workflow files[/cyan]")

        workflows = []
        for workflow_path in track(workflow_files, description="Scanning workflows..."):
            info = self.extract_workflow_info(workflow_path)
            workflows.append(info)

        return workflows

    def generate_markdown(self, workflows: List[Dict[str, Any]], output_path: Path):
        """Generate Markdown catalog.

        Args:
            workflows: List of workflow information
            output_path: Where to save the catalog
        """
        # Group by category
        by_category = defaultdict(list)
        for wf in workflows:
            by_category[wf['category']].append(wf)

        # Sort categories and workflows
        sorted_categories = sorted(by_category.keys())

        # Generate markdown
        lines = [
            "# n8n Workflow Catalog",
            "",
            f"**Total Workflows:** {len(workflows)}",
            f"**Categories:** {len(sorted_categories)}",
            "",
            "## Table of Contents",
            ""
        ]

        # TOC
        for category in sorted_categories:
            lines.append(f"- [{category}](#{category.lower().replace('_', '-').replace(' ', '-')}) ({len(by_category[category])} workflows)")

        lines.append("")
        lines.append("---")
        lines.append("")

        # Detailed sections
        for category in sorted_categories:
            lines.append(f"## {category}")
            lines.append("")

            workflows_in_cat = sorted(by_category[category], key=lambda x: x['name'])

            for wf in workflows_in_cat:
                if 'error' in wf:
                    lines.append(f"### ❌ {wf['name']}")
                    lines.append(f"**Error:** {wf['error']}")
                else:
                    lines.append(f"### {wf['name']}")
                    lines.append("")
                    lines.append(f"**Location:** `{wf['subcategory']}`")
                    lines.append("")

                    # Basic stats
                    lines.append(f"- **Nodes:** {wf['node_count']}")
                    lines.append(f"- **Connections:** {wf['connection_count']}")

                    # Trigger type
                    trigger_info = []
                    if wf['has_webhook']:
                        trigger_info.append("🌐 Webhook")
                    if wf['has_schedule']:
                        trigger_info.append("⏰ Scheduled")
                    if wf['has_manual']:
                        trigger_info.append("👆 Manual")
                    if trigger_info:
                        lines.append(f"- **Trigger:** {', '.join(trigger_info)}")

                    # Integrations
                    if wf['integrations']:
                        integrations = ', '.join(sorted(wf['integrations'])[:10])
                        if len(wf['integrations']) > 10:
                            integrations += f" (+{len(wf['integrations']) - 10} more)"
                        lines.append(f"- **Integrations:** {integrations}")

                    # Tags
                    if wf['tags']:
                        lines.append(f"- **Tags:** {', '.join(wf['tags'])}")

                lines.append("")

            lines.append("---")
            lines.append("")

        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        console.print(f"[green]Markdown catalog saved to: {output_path}[/green]")

    def generate_csv(self, workflows: List[Dict[str, Any]], output_path: Path):
        """Generate CSV catalog.

        Args:
            workflows: List of workflow information
            output_path: Where to save the CSV
        """
        import csv

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow([
                'Name', 'Category', 'Subcategory', 'Nodes', 'Connections',
                'Has Webhook', 'Has Schedule', 'Has Manual', 'Integrations',
                'Tags', 'Path'
            ])

            # Rows
            for wf in sorted(workflows, key=lambda x: (x['category'], x['name'])):
                if 'error' not in wf:
                    writer.writerow([
                        wf['name'],
                        wf['category'],
                        wf['subcategory'],
                        wf['node_count'],
                        wf['connection_count'],
                        'Yes' if wf['has_webhook'] else 'No',
                        'Yes' if wf['has_schedule'] else 'No',
                        'Yes' if wf['has_manual'] else 'No',
                        '; '.join(wf['integrations']),
                        '; '.join(wf['tags']),
                        wf['path']
                    ])

        console.print(f"[green]CSV catalog saved to: {output_path}[/green]")


@click.command()
@click.argument('root_path', type=click.Path(exists=True), default='.')
@click.option('--output', '-o', default='WORKFLOW_CATALOG.md', help='Output markdown file')
@click.option('--csv', 'csv_output', help='Also generate CSV file')
def cli(root_path: str, output: str, csv_output: str):
    """Generate a catalog of n8n workflows.

    ROOT_PATH is the directory to scan for workflows (default: current directory)
    """
    root = Path(root_path)

    catalog = WorkflowCatalog()
    workflows = catalog.scan_workflows(root)

    # Generate markdown
    output_path = Path(output)
    catalog.generate_markdown(workflows, output_path)

    # Generate CSV if requested
    if csv_output:
        csv_path = Path(csv_output)
        catalog.generate_csv(workflows, csv_path)

    console.print(f"\n[bold green]✓ Catalog generated successfully![/bold green]")
    console.print(f"  Workflows processed: {len(workflows)}")
    console.print(f"  Markdown: {output_path}")
    if csv_output:
        console.print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    cli()
