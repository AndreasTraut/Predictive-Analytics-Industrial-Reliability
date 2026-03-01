# ✈️ Flight Delay Detection — Copilot Guidelines / Copilot-Richtlinien

This file defines the project-specific rules for creating and maintaining documentation, code standards, and repository structure for the **Flight Delay Detection** project. The goal is to predict U.S. flight delays (2024 data) using an XGBoost classifier.

*Diese Datei definiert die projektspezifischen Regeln für das **Flight Delay Detection**-Projekt. Ziel ist die Vorhersage von US-Flugverspätungen (Daten 2024) mit einem XGBoost-Klassifikator.*

## 📚 Documentation Language Policy / Dokumentationssprachen-Richtlinie

### Separate Language Files / Getrennte Sprachdateien

This repository maintains **separate documentation files** for German and English:

*Dieses Repository verwendet **separate Dokumentationsdateien** für Deutsch und Englisch:*

- **README.md** — Complete German documentation / Vollständige deutsche Dokumentation
- **README_EN.md** — Complete English documentation / Vollständige englische Dokumentation

### Documentation Rules / Dokumentationsregeln

1. **No Bilingual Mixing:** Each file contains **only one language**. Do not mix German and English in the same file.
   *Kein zweisprachiges Mischen: Jede Datei enthält **nur eine Sprache**. Deutsch und Englisch nicht in derselben Datei mischen.*

2. **Cross-Reference:** Both files should reference each other at the top:
   ```markdown
   # README.md (German)
   > **English version:** [README_EN.md](README_EN.md)
   
   # README_EN.md (English)
   > **Deutsche Version:** [README.md](README.md)
   ```

3. **Content Parity:** Both files should contain the same information, just in different languages.
   *Inhaltsparität: Beide Dateien sollten dieselben Informationen enthalten, nur in verschiedenen Sprachen.*

4. **Primary Language:** German is the primary language (README.md). English is the secondary language (README_EN.md).
   *Primärsprache: Deutsch ist die Primärsprache (README.md). Englisch ist die Sekundärsprache (README_EN.md).*

5. **Update Both Files:** When making changes, update **both** README.md and README_EN.md to keep them synchronized.
   *Beide Dateien aktualisieren: Bei Änderungen **beide** README.md und README_EN.md aktualisieren, um sie synchron zu halten.*

## 📁 File Naming and Location

### Project Structure / Projektstruktur

```
Predictive-Analytics-Industrial-Reliability/
├── data/                                    # Datasets / Datensätze
│   └── flight_data_2024.csv.dvc           # DVC-managed data / DVC-verwaltete Daten
├── docs/                                    # Documentation / Dokumentation
│   └── flight_delay_insights_2024.png     # Visualizations / Visualisierungen
├── notebooks/                               # Jupyter Notebooks
│   └── flight_delay_prediction_analytics.ipynb  # Main analysis / Hauptanalyse
├── .github/
│   └── COPILOT_INSTRUCTIONS.md            # These guidelines / Diese Richtlinien
├── .gitignore
├── LICENSE
├── README.md                                # German documentation / Deutsche Dokumentation
├── README_EN.md                             # English documentation / Englische Dokumentation
└── requirements.txt
```

### Documentation Files

* **Main Documentation (German):** `README.md` in the repository root.
  * Contains project overview, installation, and quick start in German.
  * Cross-references English version: `README_EN.md`
* **Main Documentation (English):** `README_EN.md` in the repository root.
  * Contains project overview, installation, and quick start in English.
  * Cross-references German version: `README.md`
* **Changelog:** `CHANGELOG.md` in the repository root.
  * Documents all version changes, migrations, and updates.
  * Format: Markdown with clear versioning.
* **License:** `LICENSE` file in the root directory.
* **Supplementary Docs:** `docs/` directory for additional guides (e.g., `docs/SQLITE-INSTALLATION.MD`).

### Code & Assets

* **Notebooks:** `notebooks/` for Jupyter analysis notebooks (e.g., `flight_delay_prediction_analytics.ipynb`).
* **Data:** `data/` for datasets managed via DVC; never commit raw large CSV files directly.
* **Scripts:** `scripts/` for standalone tools or automation.
* **Tests:** `tests/` directory mirroring the source structure.
* **Configuration:** `requirements.txt` in the root; pin all dependency versions.

### Naming Conventions

* **Markdown Files:** 
  * `README.md` for German documentation
  * `README_EN.md` for English documentation
  * `CHANGELOG.md` in ALL_CAPS
* **Python Modules / Notebooks:** snake_case (e.g., `flight_delay_prediction_analytics.ipynb`).
* **Directories:** lowercase with underscores or hyphens.
* **Assets/Data:** Descriptive names with underscores and year suffix (e.g., `flight_data_2024.csv`).
* **Database files:** Descriptive names ending in `.db` (e.g., `flights2024.db` — domain prefix + year suffix).

## 📋 Markdown Structure

### Language Policy

**IMPORTANT:** This repository uses **separate files** for German and English documentation:
- `README.md` = German only / Nur Deutsch
- `README_EN.md` = English only / Nur Englisch

Do **not** mix languages in the same file. Each file should be written entirely in one language.

*Keine Sprachen in derselben Datei mischen. Jede Datei sollte vollständig in einer Sprache geschrieben sein.*

### README.md Requirements (applies to both German and English versions)

* **H1 Title** with Project Name and Version.
* **Introductory Paragraph** (Purpose and Value Proposition).
* **Meta Information** (Author, Date, Version).
* **Table of Contents** (📋).
* **Repository Overview** (🎯 Goals and Scope).
* **Project Structure** (📁) - Represented as an ASCII tree.
* **Quick Start Guide** (🚀).
* **Technology Stack** (📦 Versions and Dependencies).
* **Module/Feature Descriptions** (📚).
* **Installation & Setup** (🔧).
* **License & Contributions** (📝).

### Standard Metadata Block

Use blockquotes for key links and file references at the beginning of sections:

```markdown
> ➡️ **Details:** [Section-Title](#anchor-link)  
> 📖 **Implementation:** [`path/to/file.py`](path/to/file.py)  
> 🔗 **External Resource:** [Title](https://...)
```

### Formatting Rules

* **Emojis:** Use thematically appropriate emojis for headers:
  * 📁 Files/Folders | 🚀 Features/Start | ✅ Success/Done | 🔧 Setup
  * 💾 Code/Modules | 📊 Data/Analysis | ⚠️ Warning | ❓ Questions
* **Links:**
  * Use relative paths for internal files: `[Title](path/to/file)`.
  * Use absolute URLs for external resources.
* **Lists:** Use `-` for unordered and `1.` for ordered steps.

## 💻 Code Standards

### Technology Stack / Technologie-Stack

Always use and reference these project libraries — do **not** introduce alternatives without discussion:

| Library | Purpose |
|---------|---------|
| **Python 3.13** | Runtime |
| **Pandas & NumPy** | Data processing / Datenverarbeitung |
| **Scikit-learn** | Preprocessing (LabelEncoder, StandardScaler) and metrics |
| **XGBoost** | ML classifier (`n_estimators=300`, `max_depth=6`, `learning_rate=0.05`) |
| **SQLAlchemy** | SQLite database integration (`flights2024.db`, table `flight_preds_2024`) |
| **Matplotlib & Seaborn** | Visualization / Visualisierung |
| **DVC** | Data version control for large CSV files |

### ML Pipeline Conventions / ML-Pipeline-Konventionen

Follow this pipeline order in notebooks and scripts:

1. **Data Preparation:** Load `data/flight_data_2024.csv`, create target `Delayed` (1 if `arr_delay > 15`, else 0), store in SQLite.
2. **Preprocessing:** Filter cancelled/diverted flights, apply `LabelEncoder` on `op_unique_carrier`, `origin`, `dest`; apply `StandardScaler` on numeric features; 80/20 train/test split.
3. **Model Training:** Fit XGBoost classifier with the documented hyperparameters.
4. **Predictions:** Predict on the full dataset and store results in `flight_preds_2024` SQLite table.

### Python Code Blocks

* **Language:** Comments should be in English (or the specified project language), precise, and explanatory.
* **Type Hinting:** Mandatory for function parameters and return types.
* **Docstrings:** Google-style (single-line for simple, multi-line for complex logic).

```python
def process_data(input_path: str) -> bool:
    """
    Brief description of the function.
    
    Args:
        input_path: The filesystem path to the source file.
        
    Returns:
        True if successful, False otherwise.
    """
    # Step 1: Explanation of logic
    result = perform_action()
    
    return result
```

### Shell Blocks (Cross-Platform)

* Use `powershell` for Windows-specific commands.
* Use `bash` for Linux/Mac commands.
* Provide a comment above each command explaining its purpose.

## ✅ Quality Assurance

### Pre-Commit Checklist

* **Markdown Preview:** Ensure headers, tables, and lists render correctly.
* **Broken Links:** Verify all internal (anchors/files) and external links work.
* **Consistency:** Ensure the `README.md` matches the current state of the code.
* **Encoding:** Use UTF-8 for all files.
* **Line Endings:** Use LF (Unix-style).

## 🎯 Summary for AI Assistance

When generating or editing files:

* ✅ Stick to the established folder structure (`data/`, `docs/`, `notebooks/`).
* ✅ Follow naming conventions (`README.md` = German, `README_EN.md` = English, snake_case notebooks/scripts).
* ✅ Use thematic emojis for scannability.
* ✅ Include detailed comments in code blocks.
* ✅ Use metadata blockquotes for file references.
* ✅ **IMPORTANT:** Maintain separate language files — `README.md` (German only) and `README_EN.md` (English only). Do NOT mix languages in the same file.
* ✅ When updating documentation, update BOTH `README.md` and `README_EN.md` to keep them synchronized.
* ✅ Always prioritize clarity for the end-user.
* ✅ Use the defined tech stack (XGBoost, Scikit-learn, Pandas, SQLAlchemy, DVC) — do not suggest alternatives.
* ✅ Follow the ML pipeline order: Data Preparation → Preprocessing → Training → Predictions.
* ✅ Target variable is `Delayed` (1 if `arr_delay > 15`, else 0); use `DepDel15`/`ArrDel15` as feature engineering references.
* ✅ Store model predictions in SQLite (`flights2024.db`, table `flight_preds_2024`).
* ✅ Data files > 1 GB must be managed via DVC, never committed directly.

---