"""Validator for n8n workflow JSON files."""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

import click
from rich.console import Console
from rich.table import Table

console = Console(legacy_windows=False, force_terminal=True)


class N8nWorkflowValidator:
    """Validates n8n workflow JSON files."""

    REQUIRED_FIELDS = ["nodes", "connections"]
    NODE_REQUIRED_FIELDS = ["name", "type", "position"]

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_workflow(self, workflow_data: Dict[str, Any]) -> bool:
        """Validate a single workflow.

        Args:
            workflow_data: The parsed workflow JSON

        Returns:
            True if valid, False otherwise
        """
        self.errors = []
        self.warnings = []

        # Check required top-level fields
        for field in self.REQUIRED_FIELDS:
            if field not in workflow_data:
                self.errors.append(f"Missing required field: {field}")

        if self.errors:
            return False

        # Validate nodes
        nodes = workflow_data.get("nodes", [])
        if not isinstance(nodes, list):
            self.errors.append("'nodes' must be an array")
            return False

        if len(nodes) == 0:
            self.warnings.append("Workflow has no nodes")

        node_ids = set()
        for idx, node in enumerate(nodes):
            if not isinstance(node, dict):
                self.errors.append(f"Node at index {idx} is not an object")
                continue

            # Check required node fields
            for field in self.NODE_REQUIRED_FIELDS:
                if field not in node:
                    self.errors.append(f"Node at index {idx} missing required field: {field}")

            # Track node IDs/names for connection validation
            node_id = node.get("id") or node.get("name")
            if node_id:
                if node_id in node_ids:
                    self.warnings.append(f"Duplicate node identifier: {node_id}")
                node_ids.add(node_id)

            # Validate position
            position = node.get("position")
            if position and not isinstance(position, list):
                self.errors.append(f"Node '{node.get('name', idx)}' has invalid position format")

        # Validate connections
        connections = workflow_data.get("connections", {})
        if not isinstance(connections, dict):
            self.errors.append("'connections' must be an object")
        else:
            # Check that connections reference existing nodes
            for source_node, targets in connections.items():
                if source_node not in node_ids:
                    self.warnings.append(f"Connection references non-existent node: {source_node}")

        return len(self.errors) == 0

    def validate_file(self, file_path: Path) -> bool:
        """Validate a workflow file.

        Args:
            file_path: Path to the workflow JSON file

        Returns:
            True if valid, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            return self.validate_workflow(data)

        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading file: {e}")
            return False


@click.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
def cli(path: str, verbose: bool):
    """Validate n8n workflow JSON files.

    PATH can be a file or directory. If a directory, all .json files will be validated.
    """
    path_obj = Path(path)
    validator = N8nWorkflowValidator()

    # Collect files to validate
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.json"))
        # Filter out common non-workflow JSON files
        files = [f for f in files if not any(skip in str(f) for skip in ['node_modules', '.git', 'package.json', 'package-lock.json'])]

    if not files:
        console.print("[yellow]No JSON files found to validate[/yellow]")
        sys.exit(0)

    # Validate each file
    results = []
    total_errors = 0
    total_warnings = 0

    for file_path in files:
        is_valid = validator.validate_file(file_path)
        results.append({
            'file': file_path,
            'valid': is_valid,
            'errors': validator.errors.copy(),
            'warnings': validator.warnings.copy()
        })

        if not is_valid:
            total_errors += len(validator.errors)
        total_warnings += len(validator.warnings)

    # Display results
    if verbose or any(not r['valid'] for r in results):
        table = Table(title="Validation Results")
        table.add_column("File", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Issues", style="yellow")

        for result in results:
            status = "[OK] Valid" if result['valid'] else "[X] Invalid"
            status_style = "green" if result['valid'] else "red"

            issues = []
            if result['errors']:
                issues.extend([f"[red]ERROR: {e}[/red]" for e in result['errors']])
            if result['warnings']:
                issues.extend([f"[yellow]WARNING: {w}[/yellow]" for w in result['warnings']])

            issues_text = "\n".join(issues) if issues else "-"

            table.add_row(
                str(result['file'].relative_to(path_obj.parent if path_obj.is_file() else path_obj)),
                f"[{status_style}]{status}[/{status_style}]",
                issues_text
            )

        console.print(table)

    # Summary
    valid_count = sum(1 for r in results if r['valid'])
    invalid_count = len(results) - valid_count

    console.print(f"\n[bold]Summary:[/bold]")
    console.print(f"  Total files: {len(results)}")
    console.print(f"  Valid: [green]{valid_count}[/green]")
    console.print(f"  Invalid: [red]{invalid_count}[/red]")
    console.print(f"  Total errors: [red]{total_errors}[/red]")
    console.print(f"  Total warnings: [yellow]{total_warnings}[/yellow]")

    # Exit with error if any validation failed
    if invalid_count > 0:
        sys.exit(1)
    else:
        console.print("\n[green][OK] All workflows are valid![/green]")
        sys.exit(0)


if __name__ == "__main__":
    cli()
