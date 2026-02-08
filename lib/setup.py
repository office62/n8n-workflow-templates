from setuptools import setup, find_packages

setup(
    name="n8n-workflow-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jsonschema>=4.17.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "pillow>=10.0.0",
        "networkx>=3.0",
        "matplotlib>=3.7.0",
    ],
    entry_points={
        "console_scripts": [
            "n8n-validate=n8n_tools.validator:cli",
            "n8n-visualize=n8n_tools.visualizer:cli",
            "n8n-catalog=n8n_tools.catalog:cli",
        ],
    },
    python_requires=">=3.8",
)
