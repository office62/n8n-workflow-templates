# n8n Workflow Templates Collection

Colecție de peste 4000+ template-uri pentru automatizări n8n.

## 📋 Despre Proiect

Acest repository conține o colecție vastă de workflow-uri n8n organizate pe categorii:
- Analytics
- API & Webhooks
- Automation
- Communication
- Database & Storage
- Document Processing
- AI & LLMs
- Social Media
- și multe altele...

### 📚 Catalog Complet

**[Vezi WORKFLOW_CATALOG.md](WORKFLOW_CATALOG.md)** - Catalog detaliat cu toate workflow-urile

**[Descarcă WORKFLOW_CATALOG.csv](WORKFLOW_CATALOG.csv)** - Format CSV pentru Excel/Google Sheets

**Statistici:**
- **448 workflow-uri** documentate
- **7 categorii** principale
- Detalii pentru fiecare: noduri, conexiuni, trigger-uri, integrări

## ✅ Validare Automată

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

## 🛠️ Tool-uri de Validare (Local)

Poți rula validarea și local pe calculator.

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
# Generează catalog complet (Markdown + CSV)
n8n-catalog . -o WORKFLOW_CATALOG.md --csv WORKFLOW_CATALOG.csv

# Doar Markdown
n8n-catalog .
```

## 📁 Structura Repository-ului

```
.
├── .github/
│   └── workflows/
│       └── validate-workflows.yml  # GitHub Actions workflow
├── lib/
│   ├── n8n_tools/                  # Tool-uri Python de validare
│   │   ├── validator.py            # Validator de workflow-uri
│   │   └── visualizer.py           # Generator de vizualizări
│   ├── requirements.txt
│   └── setup.py
├── analytics/                      # Workflow-uri pentru analytics
├── automation/                     # Workflow-uri de automatizare
├── api-webhooks/                   # Workflow-uri API & Webhooks
└── ...                             # Alte categorii
```

## 🚀 Cum să Contribui

1. Fork repository-ul
2. Creează un branch nou: `git checkout -b feature/nume-workflow`
3. Adaugă sau modifică workflow-uri
4. Commit: `git commit -m "Add: descriere workflow"`
5. Push: `git push origin feature/nume-workflow`
6. Creează un Pull Request

Pull Request-ul tău va fi validat automat de GitHub Actions!

## 📊 Statistici

- **Total workflow-uri**: 448 (din colecția de 4000+)
- **Categorii**: 7 (analytics, automation, api-webhooks, communication, data-integration, data-transformation, document-processing)
- **Toate validate automat**: ✅
- **Catalog complet**: ✅ Markdown + CSV
- **Vizualizări auto-generate**: ✅ PNG pentru fiecare workflow

## 📝 Licență

Verifică licența fiecărui workflow individual.

---

**Made with ❤️ for the n8n community**
