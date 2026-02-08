# ✈️ Flight Delay Detection / Flugverspätungs-Erkennung

This project uses machine learning to predict flight delays based on 2024 U.S. flight data.

*Dieses Projekt nutzt Machine Learning zur Vorhersage von Flugverspätungen auf Basis von US-Flugdaten aus dem Jahr 2024.*

## 📋 Project Overview / Projektübersicht

The project includes a complete machine learning pipeline:
- Data preprocessing and feature engineering
- Training an XGBoost classifier
- Model evaluation and performance analysis
- Storing predictions in a SQLite database

*Das Projekt beinhaltet eine vollständige Machine Learning Pipeline:*
*- Datenvorverarbeitung und Feature Engineering*
*- Training eines XGBoost Klassifikators*
*- Modell-Evaluation und Leistungsanalyse*
*- Speicherung der Vorhersagen in einer SQLite-Datenbank*

# 👨‍💻 About the Authors / Über die Autoren

Swarada Kulkarni is an AI & Analytics Professional and expert on LLM Integrations. She is working with Power BI, Python. 

🔗 [Connect on LinkedIn / Vernetze dich auf LinkedIn](https://www.linkedin.com/in/swarada-kulkarni-9ab9571a0/)  
🔗 [Have a look at more examples / Schaue dir weitere, interessante BI Umsetzungen an](https://github.com/swarada431)

Andreas Traut ist ein Senior BI-Entwickler, der sich auf Data Warehousing, SQL Server und Microsoft BI Stack spezialisiert hat. 

🔗 [Connect on LinkedIn / Vernetze dich auf LinkedIn](https://www.linkedin.com/in/andreas-traut-89340/)  
🔗 [Have a look at more examples / Schaue dir weitere, interessante BI Umsetzungen an](https://github.com/AndreasTraut)

## 📊 Data Source / Datenquelle

### Flight Delay Dataset — 2024

This project uses the **Flight Delay Dataset — 2024**, available on Kaggle.

*Dieses Projekt verwendet den **Flight Delay Dataset — 2024**, der auf Kaggle verfügbar ist.*

> 🔗 **External Resource:** [Flight Data 2024 Dataset](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024/data)

### 📥 Download Details / Download-Details

There are two versions of the dataset:

*Es gibt zwei Versionen des Datensatzes:*  
| File / Datei | Rows / Zeilen | Columns / Spalten | Size / Größe | Usage / Verwendung |
|--------------|---------------|-------------------|--------------|-------------------|
| `flight_data_2024.csv` | ~7 million / ~7 Millionen | 35 | ~1.31 GB | Full dataset / Vollständiger Datensatz |
| `flight_data_2024_sample.csv` | 10,000 | 35 | ~10 MB | Sample for development / Beispieldatensatz für Entwicklung |

### 🔍 Key Features / Wichtige Features

**Feature Engineering for Delay Target / Feature Engineering für Verspätungs-Ziel:**
- `DepDel15`: Departure delay > 15 minutes / Abflugverspätung > 15 Minuten
- `ArrDel15`: Arrival delay > 15 minutes / Ankunftsverspätung > 15 Minuten

These columns can be used as the basis for creating the `Delayed` target variable.

*Diese Spalten können als Basis für die Erstellung der Zielvariable `Delayed` verwendet werden.*

### 📌 Original Source / Ursprung

The data originally comes from the **TranStats On-Time Performance database** of the U.S. Department of Transportation (Bureau of Transportation Statistics - BTS).

*Die Daten stammen ursprünglich aus der **TranStats On-Time Performance-Datenbank** des US-Verkehrsministeriums (Bureau of Transportation Statistics - BTS).*  

### 💾 SQLite Database / SQLite-Datenbank

Since the full dataset is over 1 GB, predictions are stored in a SQLite database (`flights2024.db`). This optimizes query performance and enables efficient data management.

*Da der vollständige Datensatz über 1 GB groß ist, werden die Vorhersagen in einer SQLite-Datenbank (`flights2024.db`) gespeichert. Dies optimiert die Performance bei Abfragen und ermöglicht effizientes Datenmanagement.*

> 📖 **Installation Guide:** [SQLite Installation and Usage](docs/sqlite-installation.md)

## 📂 Project Structure / Projektstruktur

```
Flight-delay-detection-/  
├── data/                                    # Datasets / Datensätze
│   └── flight_data_2024.csv.dvc           # DVC-managed data / DVC-verwaltete Daten
├── docs/                                    # Documentation / Dokumentation
│   └── flight_delay_insights_2024.png     # Visualizations / Visualisierungen
├── notebooks/                               # Jupyter Notebooks
│   └── flight_delay_prediction_analytics.ipynb  # Main analysis / Hauptanalyse
├── .gitignore                              # Git ignore rules / Git ignore Regeln
├── README.md                               # Project documentation / Projektdokumentation
└── requirements.txt                        # Python dependencies / Python Abhängigkeiten
```

## 🛠️ Tech Stack / Technologie-Stack

- **Python 3.13**
- **Pandas & NumPy** - Data processing / Datenverarbeitung
- **Scikit-learn** - Preprocessing and metrics / Preprocessing und Metriken
- **XGBoost** - Machine learning model / Machine Learning Modell
- **SQLAlchemy** - Database integration / Datenbankanbindung
- **Matplotlib & Seaborn** - Visualization / Visualisierung
- **DVC** - Data version control / Daten-Versionskontrolle

## ⚙️ Pipeline Steps / Pipeline-Schritte

### 1. Data Preparation / Datenaufbereitung
Loading flight data from `data/flight_data_2024.csv`  
Creating target variable `Delayed` (1 if `arr_delay > 15`, otherwise 0)  
Storing in SQLite database `flights2024.db`

*Laden der Flugdaten aus `data/flight_data_2024.csv`*  
*Erstellung der Zielvariable `Delayed` (1 wenn `arr_delay > 15`, sonst 0)*  
*Speicherung in SQLite-Datenbank `flights2024.db`*

### 2. Preprocessing
Filtering: Only non-cancelled and non-diverted flights  
Label encoding for categorical variables (`op_unique_carrier`, `origin`, `dest`)  
StandardScaler for numeric features  
Train/test split (80/20)

*Filterung: Nur nicht-stornierte und nicht-umgeleitete Flüge*  
*Label-Encoding für kategoriale Variablen (`op_unique_carrier`, `origin`, `dest`)*  
*StandardScaler für numerische Features*  
*Train/Test Split (80/20)*

### 3. Model Training / Modell-Training
**XGBoost Classifier Hyperparameter:**
- `n_estimators=300`
- `max_depth=6`
- `learning_rate=0.05`

### 4. Predictions / Vorhersagen
Prediction on full dataset  
Storage in SQLite table `flight_preds_2024`

*Vorhersage auf dem gesamten Datensatz*  
*Speicherung in SQLite-Tabelle `flight_preds_2024`*

## 📊 Model Performance / Modell-Performance

| Metric / Metrik | On-Time / Pünktlich (0) | Delayed / Verspätet (1) |
|-----------------|------------------------|------------------------|
| Precision       | 0.94                   | 0.92                   |
| Recall          | 0.98                   | 0.73                   |
| F1-Score        | 0.96                   | 0.81                   |

**Overall Accuracy / Gesamtgenauigkeit: ✅ 93%**

## 🚀 Installation and Usage / Installation und Ausführung

### Prerequisites / Voraussetzungen
- Python 3.13 or higher / oder höher
- Git
- DVC (for data management / für Datenverwaltung)

### Steps / Schritte

1. **Clone repository / Repository klonen:**
   ```bash
   git clone https://github.com/AndreasTraut/Flight-delay-detection-.git
   cd Flight-delay-detection-
   ```

2. **Install dependencies / Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull data (with DVC) / Daten abrufen:**
   ```bash
   dvc pull
   ```

4. **Run notebook / Notebook ausführen:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

## 📌 Next Steps / Nächste Schritte

Hyperparameter tuning for better recall on delayed flights  
Feature engineering with weather and airport congestion data  
Deployment as Flask API or Streamlit dashboard  
Integration of additional data sources

*- [ ] Hyperparameter-Tuning für besseren Recall bei verspäteten Flügen*  
*- [ ] Feature Engineering mit Wetter- und Flughafen-Auslastungsdaten*  
*- [ ] Deployment als Flask API oder Streamlit Dashboard*  
*- [ ] Integration zusätzlicher Datenquellen*

## 👤 Authors / Autoren

**Andreas Traut** & **Swarada Kulkarni**

## 📄 License / Lizenz

This project is licensed under the MIT License.

*Dieses Projekt steht unter der MIT-Lizenz.*