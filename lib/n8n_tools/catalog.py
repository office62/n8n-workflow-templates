"""Generate catalog of n8n workflows with descriptions."""

import json
import sys
import csv
from pathlib import Path
from typing import Dict, Any, List, Optional
from collections import defaultdict

import click
from rich.console import Console
from rich.progress import track

console = Console(legacy_windows=False, force_terminal=True)

# Map of common n8n node base names to human-readable service names
SERVICE_NAMES = {
    'gmail': 'Gmail',
    'googleSheets': 'Google Sheets',
    'googleDrive': 'Google Drive',
    'googleCalendar': 'Google Calendar',
    'googleDocs': 'Google Docs',
    'slack': 'Slack',
    'telegram': 'Telegram',
    'telegramTrigger': 'Telegram',
    'discord': 'Discord',
    'notion': 'Notion',
    'airtable': 'Airtable',
    'httpRequest': 'HTTP API',
    'webhook': 'Webhook',
    'postgres': 'PostgreSQL',
    'mysql': 'MySQL',
    'mongodb': 'MongoDB',
    'redis': 'Redis',
    'elasticsearch': 'Elasticsearch',
    'whatsApp': 'WhatsApp',
    'whatsapp': 'WhatsApp',
    'twitter': 'Twitter/X',
    'facebookMessenger': 'Facebook Messenger',
    'stripe': 'Stripe',
    'shopify': 'Shopify',
    'wooCommerce': 'WooCommerce',
    'wordpress': 'WordPress',
    'microsoftOutlook': 'Microsoft Outlook',
    'microsoftExcel': 'Microsoft Excel',
    'microsoftTeams': 'Microsoft Teams',
    'jira': 'Jira',
    'github': 'GitHub',
    'gitlab': 'GitLab',
    'trello': 'Trello',
    'asana': 'Asana',
    'hubspot': 'HubSpot',
    'salesforce': 'Salesforce',
    'sendGrid': 'SendGrid',
    'mailchimp': 'Mailchimp',
    'twilio': 'Twilio',
    'dropbox': 'Dropbox',
    'box': 'Box',
    'oneDrive': 'OneDrive',
    'amazonS3': 'Amazon S3',
    'awsSqs': 'AWS SQS',
    'awsSns': 'AWS SNS',
    'awsLambda': 'AWS Lambda',
    'pipedrive': 'Pipedrive',
    'typeform': 'Typeform',
    'surveyMonkey': 'SurveyMonkey',
    'webflow': 'Webflow',
    'bubble': 'Bubble',
    'supabase': 'Supabase',
    'baserow': 'Baserow',
    'nocodb': 'NocoDB',
    'ftp': 'FTP',
    'ssh': 'SSH',
    'pdf': 'PDF',
    'spreadsheetFile': 'Fișier Spreadsheet',
    'convertToFile': 'Conversie Fișier',
    'extractFromFile': 'Extracție Fișier',
    'readWriteFile': 'Fișier Local',
    'executeCommand': 'Comandă Shell',
    'respondToWebhook': 'Răspuns Webhook',
    'n8n': 'n8n Sub-workflow',
    'executeWorkflow': 'Sub-workflow',
    'openAi': 'OpenAI',
    'openAiAssistant': 'OpenAI Assistant',
    'chatOpenAi': 'OpenAI Chat',
    'lmChatOpenAi': 'OpenAI Chat',
    'lmChatOllama': 'Ollama',
    'lmChatAnthropic': 'Anthropic Claude',
    'lmChatGoogleGemini': 'Google Gemini',
    'lmChatGroq': 'Groq',
    'lmChatMistralCloud': 'Mistral AI',
    'lmChatAzureOpenAi': 'Azure OpenAI',
    'lmChatGoogleVertex': 'Google Vertex AI',
    'lmChatHuggingFace': 'HuggingFace',
    'lmChatAwsBedrock': 'AWS Bedrock',
    'memoryManager': 'Chat Memory',
    'memoryBufferWindow': 'Buffer Memory',
    'memoryPostgresChat': 'PostgreSQL Memory',
    'memoryRedisChat': 'Redis Memory',
    'memoryMotorhead': 'Motorhead Memory',
    'chainSummarization': 'LangChain Sumarizare',
    'chainLlm': 'LangChain LLM',
    'chainRetrievalQa': 'LangChain Retrieval QA',
    'vectorStoreInMemory': 'Vector Store',
    'vectorStorePinecone': 'Pinecone',
    'vectorStoreQdrant': 'Qdrant',
    'vectorStoreSupabase': 'Supabase Vector',
    'vectorStoreZep': 'Zep Vector Store',
    'embeddingsOpenAi': 'OpenAI Embeddings',
    'embeddingsMistralCloud': 'Mistral Embeddings',
    'embeddingsGoogleGemini': 'Google Embeddings',
    'embeddingsAzureOpenAi': 'Azure OpenAI Embeddings',
    'embeddingsHuggingFaceInference': 'HuggingFace Embeddings',
    'toolCalculator': 'Calculator',
    'toolCode': 'Cod Personalizat',
    'toolWorkflow': 'Sub-workflow Tool',
    'toolHttpRequest': 'HTTP Tool',
    'toolWikipedia': 'Wikipedia Tool',
    'toolSerpApi': 'SerpAPI Tool',
    'agent': 'AI Agent',
    'outputParserStructured': 'Parser Structurat',
    'outputParserAutofixing': 'Parser Autofix',
    'informationExtractor': 'Extractor Informații',
    'textClassifier': 'Clasificator Text',
    'sentimentAnalysis': 'Analiză Sentiment',
    'summarization': 'Sumarizare',
    'textSplitterRecursiveCharacterTextSplitter': 'Text Splitter',
    'textSplitterTokenTextSplitter': 'Token Splitter',
    'documentDefaultDataLoader': 'Document Loader',
    'retrieverVectorStore': 'Vector Retriever',
    'toolVectorStore': 'Vector Store Tool',
    'chatTrigger': 'Chat Trigger',
    'compression': 'Compresie',
    'editImage': 'Editor Imagine',
    'localFileTrigger': 'Monitor Fișiere Locale',
    'gmailTrigger': 'Gmail Trigger',
    'instagram': 'Instagram',
    'linkedIn': 'LinkedIn',
    'zoom': 'Zoom',
    'googleAnalytics': 'Google Analytics',
    'googleBigQuery': 'Google BigQuery',
    'microsoftSql': 'Microsoft SQL',
    'clickUp': 'ClickUp',
    'mondayCom': 'Monday.com',
    'freshdesk': 'Freshdesk',
    'zendesk': 'Zendesk',
    'intercom': 'Intercom',
    'crisp': 'Crisp',
    'todoist': 'Todoist',
    'calendly': 'Calendly',
    'contentful': 'Contentful',
    'strapi': 'Strapi',
    'ghost': 'Ghost CMS',
    'mautic': 'Mautic',
    'activeCampaign': 'ActiveCampaign',
    'convertKit': 'ConvertKit',
    'lemlist': 'Lemlist',
    'phantomBuster': 'PhantomBuster',
    'wise': 'Wise',
    'quickBooks': 'QuickBooks',
    'xero': 'Xero',
    'googleVision': 'Google Vision',
    'awsRekognition': 'AWS Rekognition',
    'nextcloud': 'Nextcloud',
    'matrix': 'Matrix',
    'mattermost': 'Mattermost',
    'rocketchat': 'Rocket.Chat',
    'line': 'LINE',
    'sms77': 'sms77',
    'vonage': 'Vonage',
    'bambooHr': 'BambooHR',
    'clockify': 'Clockify',
    'harvest': 'Harvest',
    'toggl': 'Toggl',
    'rabbitmq': 'RabbitMQ',
    'amqp': 'AMQP',
    'kafka': 'Kafka',
    'mqtt': 'MQTT',
    'graphql': 'GraphQL',
    'xml': 'XML',
    'html': 'HTML',
    'markdown': 'Markdown',
    'crypto': 'Crypto',
    'dateTime': 'Date/Time',
    'imap': 'IMAP Email',
    'emailSend': 'Email SMTP',
    'emailReadImap': 'Email IMAP',
}

# Node types that are pure utility / flow control — not worth listing as integrations
UTILITY_NODES = {
    'set', 'if', 'merge', 'code', 'function', 'functionItem', 'switch',
    'noOp', 'stickyNote', 'start', 'limit', 'aggregate', 'splitInBatches',
    'itemLists', 'removeDuplicates', 'renameKeys', 'splitOut', 'summarize',
    'filter', 'sort', 'compareDatasets', 'loop', 'executeWorkflowTrigger',
    'manualTrigger', 'errorTrigger', 'wait', 'stopAndError',
}

# Map operations to Romanian verbs
OPERATION_VERBS = {
    'send': 'trimite mesaje prin',
    'sendMessage': 'trimite mesaje prin',
    'sendPhoto': 'trimite imagini prin',
    'sendDocument': 'trimite documente prin',
    'sendAudio': 'trimite audio prin',
    'sendVideo': 'trimite video prin',
    'getAll': 'citește date din',
    'get': 'obține date din',
    'list': 'listează date din',
    'create': 'creează înregistrări în',
    'update': 'actualizează date în',
    'upsert': 'actualizează/creează în',
    'delete': 'șterge date din',
    'append': 'adaugă date în',
    'open': 'deschide sesiune în',
    'upload': 'încarcă fișiere în',
    'download': 'descarcă din',
    'search': 'caută în',
    'lookup': 'caută în',
    'execute': 'execută acțiune în',
    'getPage': 'citește pagini din',
    'createPage': 'creează pagini în',
    'updatePage': 'actualizează pagini în',
    'getDatabasePage': 'citește date din',
}


class WorkflowCatalog:
    """Creates a catalog of n8n workflows."""

    def __init__(self):
        self.workflows = []

    def _get_service_name(self, node_type: str) -> Optional[str]:
        """Get human-readable service name from a node type string."""
        if node_type.startswith('n8n-nodes-base.'):
            service = node_type.replace('n8n-nodes-base.', '')
        elif 'n8n-nodes-langchain.' in node_type:
            service = node_type.split('.')[-1]
        elif node_type.startswith('@n8n/'):
            service = node_type.split('.')[-1]
        else:
            return None

        if service in UTILITY_NODES:
            return None

        return SERVICE_NAMES.get(service, service)

    def _describe_trigger(self, nodes: list) -> str:
        """Generate a Romanian description of how the workflow is triggered."""
        for node in nodes:
            node_type = node.get('type', '').lower()
            node_name = node.get('name', '')
            params = node.get('parameters', {})

            if 'chattrigger' in node_type:
                return 'Se declanșează prin mesaj de chat'
            if 'telegramtrigger' in node_type:
                return 'Se declanșează la primirea unui mesaj Telegram'
            if 'emailtrigger' in node_type or 'imaptrigger' in node_type or 'emailreadimap' in node_type:
                return 'Se declanșează la primirea unui email'
            if 'formtrigger' in node_type or 'n8nformtrigger' in node_type:
                return 'Se declanșează la trimiterea unui formular n8n'
            if 'webhook' in node_type and 'respond' not in node_type:
                return 'Se declanșează prin webhook HTTP'
            if 'scheduletrigger' in node_type:
                rule = params.get('rule', {})
                intervals = rule.get('interval', [{}])
                if intervals and isinstance(intervals[0], dict):
                    hour = intervals[0].get('triggerAtHour')
                    if hour is not None:
                        return f'Rulează zilnic la ora {hour}:00'
                return 'Rulează programat (schedule)'
            if 'cron' in node_type:
                return 'Rulează programat (cron)'
            if 'manualtrigger' in node_type:
                return 'Se declanșează manual'

            # Generic trigger detection
            if 'trigger' in node_type:
                service = self._get_service_name(node.get('type', ''))
                if service:
                    return f'Se declanșează de {service}'
                # Use node name as fallback
                if node_name and node_name.lower() != 'trigger':
                    return f'Se declanșează de {node_name}'

        return 'Declanșare manuală sau nedeterminată'

    def _describe_actions(self, nodes: list) -> List[str]:
        """Build a list of human-readable action strings from non-trigger nodes."""
        actions = []
        seen = set()

        for node in nodes:
            node_type = node.get('type', '')
            node_type_lower = node_type.lower()

            # Skip triggers, sticky notes, and utility nodes
            if any(kw in node_type_lower for kw in ('trigger', 'cron', 'stickynote', 'start')):
                continue

            service = self._get_service_name(node_type)
            if not service:
                continue

            params = node.get('parameters', {})
            operation = params.get('operation', '')
            resource = params.get('resource', '')

            key = f"{service}:{operation}"
            if key in seen:
                continue
            seen.add(key)

            if operation and operation in OPERATION_VERBS:
                actions.append(f"{OPERATION_VERBS[operation]} {service}")
            elif service:
                actions.append(f"folosește {service}")

        return actions

    def _get_sticky_notes_text(self, nodes: list) -> str:
        """Extract useful documentation from sticky notes (first meaningful one)."""
        notes = []
        for node in nodes:
            if 'stickyNote' in node.get('type', ''):
                content = node.get('parameters', {}).get('content', '').strip()
                # Remove markdown headings for cleaner text
                clean = content.replace('####', '').replace('###', '').replace('##', '').replace('#', '').strip()
                if len(clean) > 15:
                    notes.append(clean)

        if not notes:
            return ''

        # Return the longest note (usually most informative), capped
        best = max(notes, key=len)
        if len(best) > 250:
            best = best[:250].rsplit(' ', 1)[0] + '...'
        return best

    def generate_description(self, data: dict, name: str) -> str:
        """Generate a Romanian description of what the workflow does."""
        nodes = data.get('nodes', [])

        if not nodes:
            return 'Workflow gol (fără noduri).'

        parts = []

        # 1. Trigger
        trigger = self._describe_trigger(nodes)
        parts.append(trigger)

        # 2. Actions
        actions = self._describe_actions(nodes)
        if actions:
            if len(actions) == 1:
                parts.append(actions[0])
            elif len(actions) <= 4:
                parts.append(', '.join(actions))
            else:
                parts.append(', '.join(actions[:4]) + f' (+{len(actions) - 4} altele)')

        desc = '. '.join(parts)
        if not desc.endswith('.'):
            desc += '.'

        # 3. Add sticky note context if useful
        sticky = self._get_sticky_notes_text(nodes)
        if sticky:
            desc += f' Detalii: {sticky}'

        return desc

    def extract_workflow_info(self, workflow_path: Path) -> Dict[str, Any]:
        """Extract information from a workflow file.

        Args:
            workflow_path: Path to the workflow JSON or TXT file

        Returns:
            Dictionary with workflow information
        """
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Determine name and category based on file type
            if workflow_path.suffix == '.txt':
                name = data.get('name', workflow_path.stem)
                category = workflow_path.parent.name
                subcategory = ''
            else:
                name = data.get('name', workflow_path.parent.name)
                category = workflow_path.parent.parent.name
                subcategory = workflow_path.parent.name

            nodes = data.get('nodes', [])
            connections = data.get('connections', {})
            tags = data.get('tags', [])

            # Count node types and identify integrations/triggers
            node_types = defaultdict(int)
            trigger_types = []
            integration_nodes = []

            for node in nodes:
                node_type = node.get('type', '')
                node_types[node_type] += 1

                is_trigger = any(kw in node_type.lower() for kw in ('trigger', 'cron'))
                if is_trigger:
                    trigger_types.append(node.get('name', node_type))

                # Don't add triggers or sticky notes to integration list
                if not is_trigger and 'stickyNote' not in node_type:
                    service = self._get_service_name(node_type)
                    if service:
                        integration_nodes.append(service)

            # Generate description
            description = self.generate_description(data, name)

            return {
                'name': name,
                'path': str(workflow_path),
                'category': category,
                'subcategory': subcategory,
                'description': description,
                'node_count': len(nodes),
                'connection_count': len(connections),
                'triggers': list(set(trigger_types)),
                'integrations': list(set(integration_nodes)),
                'tags': [
                    tag.get('name') if isinstance(tag, dict) else str(tag)
                    for tag in tags
                ],
                'has_webhook': any('webhook' in nt.lower() for nt in node_types.keys()),
                'has_schedule': any(
                    'schedule' in nt.lower() or 'cron' in nt.lower()
                    for nt in node_types.keys()
                ),
                'has_manual': any('manual' in nt.lower() for nt in node_types.keys()),
            }
        except json.JSONDecodeError:
            return {
                'name': workflow_path.stem,
                'path': str(workflow_path),
                'error': f'JSON invalid în {workflow_path.name}',
                'category': workflow_path.parent.name,
                'subcategory': '',
            }
        except Exception as e:
            return {
                'name': workflow_path.stem,
                'path': str(workflow_path),
                'error': str(e),
                'category': workflow_path.parent.name,
                'subcategory': '',
            }

    def scan_workflows(self, root_path: Path) -> List[Dict[str, Any]]:
        """Scan directory for workflow files (.json and .txt).

        Args:
            root_path: Root directory to scan

        Returns:
            List of workflow information dictionaries
        """
        skip_dirs = ['node_modules', '.git', 'lib', '.github']

        # Find workflow.json files in numbered subdirectories
        json_files = [
            f for f in root_path.rglob("workflow.json")
            if not any(skip in str(f) for skip in skip_dirs)
        ]

        # Find .txt files that may contain workflow JSON
        txt_files = [
            f for f in root_path.rglob("*.txt")
            if not any(skip in str(f) for skip in skip_dirs)
        ]

        all_files = json_files + txt_files

        console.print(f"[cyan]Găsite {len(json_files)} fișiere workflow.json[/cyan]")
        console.print(f"[cyan]Găsite {len(txt_files)} fișiere .txt cu workflow-uri[/cyan]")
        console.print(f"[cyan]Total: {len(all_files)} fișiere de procesat[/cyan]")

        workflows = []
        for workflow_path in track(all_files, description="Se scanează workflow-urile..."):
            info = self.extract_workflow_info(workflow_path)
            workflows.append(info)

        return workflows

    def generate_markdown(self, workflows: List[Dict[str, Any]], output_path: Path):
        """Generate Markdown catalog with descriptions.

        Args:
            workflows: List of workflow information
            output_path: Where to save the catalog
        """
        # Group by category (replace underscores with spaces for display)
        by_category = defaultdict(list)
        for wf in workflows:
            display_cat = wf['category'].replace('_', ' ')
            by_category[display_cat].append(wf)

        sorted_categories = sorted(by_category.keys())
        total_valid = sum(1 for wf in workflows if 'error' not in wf)
        total_errors = sum(1 for wf in workflows if 'error' in wf)

        lines = [
            "# n8n Workflow Catalog",
            "",
            f"**Total workflow-uri:** {len(workflows)} ({total_valid} valide, {total_errors} cu erori)",
            f"**Categorii:** {len(sorted_categories)}",
            "",
            "## Cuprins",
            ""
        ]

        # Table of Contents
        for category in sorted_categories:
            anchor = category.lower().replace(' ', '-').replace('_', '-')
            count = len(by_category[category])
            lines.append(f"- [{category}](#{anchor}) ({count} workflow-uri)")

        lines.append("")
        lines.append("---")
        lines.append("")

        # Detailed sections per category
        for category in sorted_categories:
            lines.append(f"## {category}")
            lines.append("")

            workflows_in_cat = sorted(by_category[category], key=lambda x: x['name'])

            for wf in workflows_in_cat:
                if 'error' in wf:
                    lines.append(f"### ❌ {wf['name']}")
                    lines.append(f"**Eroare:** {wf['error']}")
                    lines.append("")
                    continue

                lines.append(f"### {wf['name']}")
                lines.append("")

                # Description as blockquote
                if wf.get('description'):
                    lines.append(f"> {wf['description']}")
                    lines.append("")

                if wf.get('subcategory'):
                    lines.append(f"**Locație:** `{wf['subcategory']}`")
                    lines.append("")

                # Stats
                lines.append(f"- **Noduri:** {wf['node_count']}")
                lines.append(f"- **Conexiuni:** {wf['connection_count']}")

                # Trigger type
                trigger_info = []
                if wf['has_webhook']:
                    trigger_info.append("🌐 Webhook")
                if wf['has_schedule']:
                    trigger_info.append("⏰ Programat")
                if wf['has_manual']:
                    trigger_info.append("👆 Manual")
                if trigger_info:
                    lines.append(f"- **Declanșare:** {', '.join(trigger_info)}")

                # Integrations
                if wf['integrations']:
                    sorted_integ = sorted(set(wf['integrations']))
                    display = ', '.join(sorted_integ[:10])
                    if len(sorted_integ) > 10:
                        display += f" (+{len(sorted_integ) - 10} altele)"
                    lines.append(f"- **Integrări:** {display}")

                # Tags
                if wf['tags']:
                    lines.append(f"- **Tag-uri:** {', '.join(wf['tags'])}")

                lines.append("")

            lines.append("---")
            lines.append("")

        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        console.print(f"[green]Catalog Markdown salvat: {output_path}[/green]")

    def generate_csv(self, workflows: List[Dict[str, Any]], output_path: Path):
        """Generate CSV catalog with descriptions.

        Args:
            workflows: List of workflow information
            output_path: Where to save the CSV
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow([
                'Name', 'Category', 'Subcategory', 'Description',
                'Nodes', 'Connections',
                'Has Webhook', 'Has Schedule', 'Has Manual',
                'Integrations', 'Tags', 'Path'
            ])

            for wf in sorted(workflows, key=lambda x: (x['category'], x['name'])):
                if 'error' not in wf:
                    writer.writerow([
                        wf['name'],
                        wf['category'],
                        wf.get('subcategory', ''),
                        wf.get('description', ''),
                        wf['node_count'],
                        wf['connection_count'],
                        'Yes' if wf['has_webhook'] else 'No',
                        'Yes' if wf['has_schedule'] else 'No',
                        'Yes' if wf['has_manual'] else 'No',
                        '; '.join(sorted(set(wf['integrations']))),
                        '; '.join(wf['tags']),
                        wf['path']
                    ])

        console.print(f"[green]Catalog CSV salvat: {output_path}[/green]")


@click.command()
@click.argument('root_path', type=click.Path(exists=True), default='.')
@click.option('--output', '-o', default='WORKFLOW_CATALOG.md', help='Fișier Markdown de ieșire')
@click.option('--csv', 'csv_output', help='Generează și fișier CSV')
def cli(root_path: str, output: str, csv_output: str):
    """Generate a catalog of n8n workflows.

    ROOT_PATH is the directory to scan for workflows (default: current directory).
    Scans both workflow.json and .txt files containing workflow definitions.
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

    # Summary
    valid = sum(1 for w in workflows if 'error' not in w)
    errors = sum(1 for w in workflows if 'error' in w)
    categories = len(set(w['category'] for w in workflows))

    console.print(f"\n[bold green]✓ Catalog generat cu succes![/bold green]")
    console.print(f"  Workflow-uri procesate: {len(workflows)} ({valid} valide, {errors} cu erori)")
    console.print(f"  Categorii: {categories}")
    console.print(f"  Markdown: {output_path}")
    if csv_output:
        console.print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    cli()
