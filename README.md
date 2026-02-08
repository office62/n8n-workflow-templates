# n8n Workflow Templates Collection

Colecție de **740 workflow-uri n8n** organizate pe **24 de categorii**, cu descrieri auto-generate pentru fiecare.

## Despre Proiect

Acest repository conține workflow-uri n8n gata de utilizat, acoperind o gamă largă de integrări și cazuri de utilizare:

| Categorie | Workflow-uri | Descriere |
|-----------|:-----------:|-----------|
| AI Research, RAG & Data Analysis | 41 | Crawlere AI, RAG cu Qdrant/Pinecone, analiză date |
| OpenAI & LLMs | 82 | Chatboți, asistenți AI, generare conținut, clasificare |
| Automation | 252 | Automatizări generale, cron jobs, integrări multiple |
| Data Integration | 75 | Sincronizare date între servicii, ETL |
| Communication | 41 | Email, Slack, notificări, mesagerie |
| Document Processing | 30 | Procesare PDF, OCR, conversii documente |
| Data Transformation | 24 | Transformare, filtrare, agregare date |
| Gmail & Email | 21 | Automatizări email, filtre, sumarizare cu AI |
| API & Webhooks | 20 | Integrări API, webhook handlers |
| Telegram | 20 | Boți Telegram, notificări, comenzi |
| Google Drive & Sheets | 17 | Automatizări Google Workspace |
| PDF & Documents | 18 | Procesare PDF cu AI, extracție date |
| Slack | 11 | Integrări și automatizări Slack |
| Instagram, Twitter & Social Media | 10 | Publicare, monitorizare social media |
| Notion | 10 | Automatizări Notion, sincronizare |
| WordPress | 6 | Publicare, management conținut |
| Analytics | 6 | Tracking, rapoarte, dashboards |
| Alte categorii | 56 | Airtable, Discord, WhatsApp, HR, Forms, etc. |

### Catalog Complet

**[WORKFLOW_CATALOG.md](WORKFLOW_CATALOG.md)** - Catalog detaliat cu descrierea fiecărui workflow

**[WORKFLOW_CATALOG.csv](WORKFLOW_CATALOG.csv)** - Format CSV pentru Excel/Google Sheets

Fiecare workflow include:
- **Descriere automată** a ce face (trigger, acțiuni, integrări)
- Număr de noduri și conexiuni
- Tip de declanșare (webhook, programat, manual)
- Lista de integrări utilizate
- Tag-uri și metadate

## Validare Automată

Acest repository folosește GitHub Actions pentru a valida automat toate workflow-urile n8n.

### Cum funcționează?

1. **Push/Pull Request**: Când faci push sau creezi un PR, workflow-ul de validare se execută automat
2. **Validare**: Toate fișierele JSON sunt validate pentru a fi sigur că sunt workflow-uri n8n valide
3. **Vizualizări**: Se creează automat diagrame vizuale pentru fiecare workflow
4. **Artifacts**: Imaginile PNG cu vizualizările sunt disponibile pentru download timp de 7 zile

### Rulare Manuală

Poți rula workflow-ul manual din tab-ul "Actions" pe GitHub:
1. Mergi la tab-ul **Actions**
2. Selectează "Validate n8n Workflows"
3. Click pe **Run workflow**

## Tool-uri (Local)

Poți rula validarea și generarea de catalog local pe calculator.

### Instalare

```bash
cd lib
pip install -e .
```

### Utilizare

**Validare workflow:**
```bash
# Validează un singur fișier
n8n-validate path/to/workflow.json

# Validează toate workflow-urile dintr-un director
n8n-validate analytics/

# Validează tot repository-ul
n8n-validate .
```

**Creare vizualizări:**
```bash
# Creează o imagine PNG pentru un workflow
n8n-visualize path/to/workflow.json -o output.png

# Fără afișare automată
n8n-visualize path/to/workflow.json -o output.png --no-show
```

**Generare catalog:**
```bash
# Generează catalog complet (Markdown + CSV) cu descrieri
n8n-catalog . -o WORKFLOW_CATALOG.md --csv WORKFLOW_CATALOG.csv

# Doar Markdown
n8n-catalog .
```

Catalogul scanează atât fișiere `workflow.json` cât și `.txt` care conțin definiții de workflow-uri n8n.

## Structura Repository-ului

```
.
├── .github/
│   └── workflows/
│       └── validate-workflows.yml    # GitHub Actions CI
├── lib/
│   ├── n8n_tools/
│   │   ├── validator.py              # Validator workflow-uri
│   │   ├── visualizer.py             # Generator vizualizări PNG
│   │   └── catalog.py                # Generator catalog cu descrieri
│   ├── requirements.txt
│   └── setup.py
├── AI_Research_RAG_and_Data_Analysis/ # RAG, crawlere AI, analiză
├── OpenAI_and_LLMs/                  # Chatboți, asistenți, LLM-uri
├── automation/                       # Automatizări generale
├── data-integration/                 # Sincronizare date, ETL
├── communication/                    # Email, Slack, notificări
├── Telegram/                         # Boți și automatizări Telegram
├── Gmail_and_Email_Automation/       # Automatizări email
├── Google_Drive_and_Google_Sheets/   # Google Workspace
├── ...                               # + 16 alte categorii
├── WORKFLOW_CATALOG.md               # Catalog complet Markdown
├── WORKFLOW_CATALOG.csv              # Catalog CSV
└── INSTRUCTIUNI_GITHUB.md            # Instrucțiuni setup GitHub
```

## Cum să Contribui

1. Fork repository-ul
2. Creează un branch nou: `git checkout -b feature/nume-workflow`
3. Adaugă sau modifică workflow-uri
4. Commit: `git commit -m "Add: descriere workflow"`
5. Push: `git push origin feature/nume-workflow`
6. Creează un Pull Request

Pull Request-ul tău va fi validat automat de GitHub Actions!

## Statistici

- **Total workflow-uri**: 740
- **Categorii**: 24
- **Formate**: workflow.json (448) + .txt (292)
- **Toate cu descrieri auto-generate**
- **Validare automată**: GitHub Actions
- **Catalog**: Markdown + CSV cu descrieri

## Licență

Verifică licența fiecărui workflow individual.

---

**Made with ❤️ for the n8n community**
