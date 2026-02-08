"""Visualizer for n8n workflow JSON files."""

import json
import sys
from pathlib import Path
from typing import Dict, Any

import click
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


class N8nWorkflowVisualizer:
    """Creates visual representations of n8n workflows."""

    def __init__(self):
        self.graph = nx.DiGraph()

    def visualize_workflow(self, workflow_data: Dict[str, Any], output_path: Path, show: bool = True):
        """Create a visualization of a workflow.

        Args:
            workflow_data: The parsed workflow JSON
            output_path: Where to save the visualization
            show: Whether to display the visualization
        """
        self.graph.clear()

        # Extract nodes
        nodes = workflow_data.get("nodes", [])
        connections = workflow_data.get("connections", {})

        # Add nodes to graph
        node_labels = {}
        node_colors = []

        for node in nodes:
            node_id = node.get("id", node.get("name"))
            node_name = node.get("name", node_id)
            node_type = node.get("type", "unknown")

            self.graph.add_node(node_id)
            node_labels[node_id] = f"{node_name}\n({node_type})"

            # Color nodes by type
            if node_type.startswith("n8n-nodes-base.start"):
                node_colors.append('#4CAF50')  # Green for start
            elif node_type.startswith("n8n-nodes-base.set"):
                node_colors.append('#2196F3')  # Blue for set
            elif node_type.startswith("n8n-nodes-base.if"):
                node_colors.append('#FF9800')  # Orange for conditionals
            elif "http" in node_type.lower() or "webhook" in node_type.lower():
                node_colors.append('#9C27B0')  # Purple for HTTP/webhooks
            else:
                node_colors.append('#757575')  # Gray for others

        # Add edges from connections
        for source_id, outputs in connections.items():
            if not isinstance(outputs, dict):
                continue

            for output_name, connections_list in outputs.items():
                if not isinstance(connections_list, list):
                    continue

                for connection in connections_list:
                    if isinstance(connection, dict):
                        target_id = connection.get("node")
                        if target_id:
                            self.graph.add_edge(source_id, target_id)

        # Create visualization
        plt.figure(figsize=(16, 12))

        # Use hierarchical layout if possible
        try:
            pos = nx.spring_layout(self.graph, k=2, iterations=50)
        except:
            pos = nx.random_layout(self.graph)

        # Draw the graph
        nx.draw_networkx_nodes(
            self.graph, pos,
            node_color=node_colors,
            node_size=3000,
            alpha=0.9
        )

        nx.draw_networkx_labels(
            self.graph, pos,
            node_labels,
            font_size=8,
            font_weight='bold'
        )

        nx.draw_networkx_edges(
            self.graph, pos,
            edge_color='#333333',
            arrows=True,
            arrowsize=20,
            arrowstyle='->',
            width=2,
            alpha=0.6
        )

        # Add title
        workflow_name = workflow_data.get("name", "Unnamed Workflow")
        plt.title(f"n8n Workflow: {workflow_name}", fontsize=16, fontweight='bold')

        plt.axis('off')
        plt.tight_layout()

        # Save the figure
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150, bbox_inches='tight')

        if show:
            plt.show()
        else:
            plt.close()


@click.command()
@click.argument('workflow_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path (PNG)')
@click.option('--show/--no-show', default=True, help='Display the visualization')
def cli(workflow_file: str, output: str, show: bool):
    """Visualize an n8n workflow JSON file.

    Creates a graph visualization showing nodes and their connections.
    """
    workflow_path = Path(workflow_file)

    # Determine output path
    if output:
        output_path = Path(output)
    else:
        output_path = workflow_path.parent / f"{workflow_path.stem}_visualization.png"

    # Load workflow
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)
    except Exception as e:
        click.echo(f"Error loading workflow: {e}", err=True)
        sys.exit(1)

    # Create visualization
    try:
        visualizer = N8nWorkflowVisualizer()
        visualizer.visualize_workflow(workflow_data, output_path, show=show)
        click.echo(f"Visualization saved to: {output_path}")
    except Exception as e:
        click.echo(f"Error creating visualization: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
