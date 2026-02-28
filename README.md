# ✈️ Flight Delay Detection / Flugverspätungs-Erkennung

This project uses machine learning to predict flight delays based on 2024 U.S. flight data.

*Dieses Projekt nutzt Machine Learning zur Vorhersage von Flugverspätungen auf Basis von US-Flugdaten aus dem Jahr 2024.*

## 🔭 Project Overview: The Science of Availability

This repository demonstrates how data science can be used to predict and prevent disruptions in complex systems. Whether it's a plane delayed on the tarmac or a crane failing on a construction site, the mathematical approach remains the same:

* **Aviation Logistics:** Predicting delays using historical flight data.
* **Root Cause Analysis (RCA):** Identifying why a mechanical system (crane) failed.
* **Predictive Maintenance (PdM):** Estimating when a component needs service before it breaks.

---

## 📋 Pipeline Overview / Pipeline-Übersicht

The project includes two complete machine learning pipelines:

**✈️ Flight Delay Detection**
- Data preprocessing and feature engineering
- Training an XGBoost classifier
- Model evaluation and performance analysis
- Storing predictions in a SQLite database

**🏗️ Crane Predictive Maintenance & RCA**
- Synthetic dataset generation (see `scripts/generate_crane_dataset.py`)
- Root Cause Analysis: XGBoost fault classifier (`Normal` / `E102_Motor_Overheat` / `E505_Bearing_Issue`)
- Predictive Maintenance: Linear regression forecast for brake pad replacement

*Das Projekt enthält zwei vollständige Machine Learning Pipelines:*

*✈️ Flugverspätungs-Erkennung*
*- Datenvorverarbeitung und Feature Engineering*
*- Training eines XGBoost Klassifikators*
*- Modell-Evaluation und Leistungsanalyse*
*- Speicherung der Vorhersagen in einer SQLite-Datenbank*

*🏗️ Kran Predictive Maintenance & RCA*
*- Synthetische Datensatzerzeugung (siehe `scripts/generate_crane_dataset.py`)*
*- Root Cause Analysis: XGBoost-Fehlerklassifikator (`Normal` / `E102_Motor_Overheat` / `E505_Bearing_Issue`)*
*- Predictive Maintenance: Lineare Regression zur Vorhersage des Bremsbelag-Austauschs*

## 👨‍💻 About the Authors / Über die Autoren

Swarada Kulkarni is an AI & Analytics Professional and expert on LLM Integrations. She is working with Power BI and Python.   
*Swarada Kulkarni ist Expertin für KI und Analytik und Spezialistin für LLM-Integrationen. Sie arbeitet mit Power BI und Python.*

🔗 [Connect on LinkedIn / Vernetze dich auf LinkedIn](https://www.linkedin.com/in/swarada-kulkarni-9ab9571a0/)  
🔗 [Have a look at more examples / Schaue dir weitere, interessante BI Umsetzungen an](https://github.com/swarada431)

Andreas Traut is a senior BI developer specializing in data warehousing, SQL Server, and Microsoft BI Stack.   
*Andreas Traut ist ein Senior BI-Entwickler, der sich auf Data Warehousing, SQL Server und Microsoft BI Stack spezialisiert hat.* 

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

> 📖 **Installation Guide:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

---

### 🏗️ Crane Maintenance Dataset — Synthetic / Kran-Wartungsdatensatz — Synthetisch

This project also includes a **synthetic crane drive dataset** generated with `scripts/generate_crane_dataset.py`.  It simulates 1,000 hourly sensor readings from a bridge or tower crane hoist unit with injected fault patterns.

*Dieses Projekt enthält außerdem einen **synthetischen Kran-Antriebsdatensatz**, der mit `scripts/generate_crane_dataset.py` erzeugt wird.  Er simuliert 1.000 stündliche Sensormesswerte eines Brücken- oder Turmdrehkran-Hubwerks mit eingebetteten Fehlermustern.*

> 📖 **Implementation:** [`scripts/generate_crane_dataset.py`](scripts/generate_crane_dataset.py)  
> 📖 **Analysis Notebook:** [`notebooks/crane_maintenance_analytics.ipynb`](notebooks/crane_maintenance_analytics.ipynb)

### 🔍 Crane Dataset Features / Kran-Datensatz Features

| Feature | Description / Beschreibung | Relevance / Bedeutung |
|---------|---------------------------|----------------------|
| `Timestamp` | Hourly observation timestamp / Stündlicher Zeitstempel | Time axis for trend analysis / Zeitachse für Trendanalyse |
| `Load_kg` | Current hook load / Aktuelle Last am Haken | Overload accelerates wear / Überlastung beschleunigt Verschleiß |
| `Motor_Temp` | Hoist motor temperature (°C) / Motortemperatur (°C) | Systematic overheating shortens insulation life / Systematische Überhitzung verkürzt die Isolationslebensdauer |
| `Vibration` | Vibration at hoist unit (mm/s) / Schwingung am Hubwerk (mm/s) | RCA: high values indicate bearing/gearbox fault / RCA: Hohe Werte deuten auf Lager-/Getriebedefekt hin |
| `Brake_Wear` | Remaining brake pad thickness (mm) / Verbleibende Belagdicke (mm) | Direct wear measure / Direktes Verschleißmaß |
| `Error_Code` | Fault label (target variable) / Fehlerbezeichnung (Zielvariable) | `Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue` |

### 🚀 Regenerate the Dataset / Datensatz neu erzeugen

```bash
python scripts/generate_crane_dataset.py
```

## 📂 Project Structure / Projektstruktur

```
Predictive-Analytics-Industrial-Reliability/
├── data/                                          # Datasets / Datensätze
│   ├── flight_data_2024.csv.dvc                 # DVC-managed data / DVC-verwaltete Daten
│   └── kran_wartung_daten.csv                   # Synthetic crane dataset / Synthetischer Kran-Datensatz
├── docs/                                          # Documentation / Dokumentation
│   ├── flight_delay_insights_2024.png           # Flight visualizations / Flug-Visualisierungen
│   └── crane_maintenance_insights.png           # Crane visualizations / Kran-Visualisierungen
├── notebooks/                                     # Jupyter Notebooks
│   ├── flight_delay_prediction_analytics.ipynb  # Flight delay analysis / Flugverspätungs-Analyse
│   └── crane_maintenance_analytics.ipynb        # Crane PdM & RCA analysis / Kran PdM & RCA
├── scripts/                                       # Standalone tools / Eigenständige Skripte
│   └── generate_crane_dataset.py               # Crane dataset generator / Kran-Datensatz-Generator
├── .gitignore                                     # Git ignore rules / Git ignore Regeln
├── README.md                                      # Project documentation / Projektdokumentation
└── requirements.txt                               # Python dependencies / Python Abhängigkeiten
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