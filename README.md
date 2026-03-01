# 🏭 Predictive Analytics for Industrial Reliability v1.0 / Prädiktive Analytik für industrielle Zuverlässigkeit v1.0

This project demonstrates the universal applicability of predictive analytics across diverse industries. It showcases two complete machine learning pipelines:

**✈️ Flight Delay Prediction:** Using historical U.S. flight data from 2024, an XGBoost classifier predicts arrival delays with 93% accuracy. The model analyzes patterns in carrier performance, routes, and operational metrics to identify flights at risk of delays greater than 15 minutes.

**🏗️ Crane Predictive Maintenance & Root Cause Analysis:** A synthetic dataset simulates sensor readings from industrial crane hoist systems. The pipeline combines XGBoost classification for fault diagnosis (`Normal`, `Motor_Overheat`, `Bearing_Issue`) with linear regression to forecast brake pad replacement timing, preventing unexpected equipment downtime.

Both use cases demonstrate how the same data science methodologies—feature engineering, supervised learning, and performance optimization—can predict and prevent disruptions in complex operational systems.

---

*Dieses Projekt demonstriert die universelle Anwendbarkeit prädiktiver Analytik über verschiedene Branchen hinweg. Es präsentiert zwei vollständige Machine Learning Pipelines:*

**✈️ Flugverspätungs-Vorhersage:** Basierend auf historischen US-Flugdaten von 2024 sagt ein XGBoost-Klassifikator Ankunftsverspätungen mit 93% Genauigkeit voraus. Das Modell analysiert Muster in der Carrier-Performance, Routen und betrieblichen Kennzahlen, um Flüge zu identifizieren, die ein Verspätungsrisiko von über 15 Minuten aufweisen.*

**🏗️ Kran Predictive Maintenance & Ursachenanalyse:** Ein synthetischer Datensatz simuliert Sensormesswerte von industriellen Kran-Hubwerken. Die Pipeline kombiniert XGBoost-Klassifikation zur Fehlerdiagnose (`Normal`, `Motor_Overheat`, `Bearing_Issue`) mit linearer Regression zur Vorhersage des Bremsbelag-Austauschzeitpunkts und verhindert so ungeplante Anlagenausfälle.*

*Beide Anwendungsfälle zeigen, wie dieselben Data Science Methoden – Feature Engineering, überwachtes Lernen und Performance-Optimierung – Störungen in komplexen operativen Systemen vorhersagen und verhindern können.*

---

## 👨‍💻 About the Authors / Über die Autoren

### 👨‍💻 Authors / Autoren

**Swarada Kulkarni** — AI & Analytics Professional, expert on LLM Integrations, Power BI and Python.  
*Swarada Kulkarni ist Expertin für KI und Analytik und Spezialistin für LLM-Integrationen. Sie arbeitet mit Power BI und Python.*

🔗 [Connect on LinkedIn / Vernetze dich auf LinkedIn](https://www.linkedin.com/in/swarada-kulkarni-9ab9571a0/)  
🔗 [Have a look at more examples / Schaue dir weitere Beispiele an](https://github.com/swarada431)

**Andreas Traut** — Senior BI developer specializing in data warehousing, SQL Server, and Microsoft BI Stack.  
*Andreas Traut ist ein Senior BI-Entwickler, der sich auf Data Warehousing, SQL Server und Microsoft BI Stack spezialisiert hat.*

🔗 [Connect on LinkedIn / Vernetze dich auf LinkedIn](https://www.linkedin.com/in/andreas-traut-89340/)  
🔗 [Have a look at more examples / Schaue dir weitere Beispiele an](https://github.com/AndreasTraut)



---

## 📋 Table of Contents / Inhaltsverzeichnis

- [🎯 Repository Overview](#-repository-overview--projektübersicht)
- [📁 Project Structure](#-project-structure--projektstruktur)
- [🚀 Quick Start Guide](#-quick-start-guide--schnellstart)
- [📦 Technology Stack](#-technology-stack--technologie-stack)
- [📊 Data Source](#-data-source--datenquelle)
- [📚 Module and Feature Descriptions](#-module-and-feature-descriptions--modul--und-funktionsbeschreibungen)
- [🔧 Installation & Setup](#-installation--setup--installation-und-einrichtung)
- [📊 Model Performance](#-model-performance--modell-performance)
- [📌 Next Steps](#-next-steps--nächste-schritte)
- [📝 License & Contributions](#-license--contributions--lizenz-und-beiträge)

---

## 🎯 Repository Overview / Projektübersicht

This repository demonstrates how data science can be used to predict and prevent disruptions in complex systems. Whether it's a plane delayed on the tarmac or a crane failing on a construction site, the mathematical approach remains the same:

*Dieses Repository zeigt, wie Data Science eingesetzt werden kann, um Störungen in komplexen Systemen vorherzusagen und zu verhindern. Ob ein Flugzeug auf dem Rollfeld verspätet ist oder ein Kran auf einer Baustelle ausfällt – der mathematische Ansatz bleibt derselbe:*

- **Aviation Logistics:** Predicting delays using historical flight data.  
  *Luftfahrtlogistik: Vorhersage von Verspätungen anhand historischer Flugdaten.*
- **Root Cause Analysis (RCA):** Identifying why a mechanical system (crane) failed.  
  *Ursachenanalyse (RCA): Ermittlung der Ursache für den Ausfall eines mechanischen Systems (Kran).*
- **Predictive Maintenance (PdM):** Estimating when a component needs service before it breaks.  
  *Predictive Maintenance (PdM): Schätzung des Servicezeitpunkts einer Komponente, bevor sie ausfällt.*

---

## 📁 Project Structure / Projektstruktur

```
Predictive-Analytics-Industrial-Reliability/
├── data/                                          # Datasets / Datensätze
│   ├── flight_data_2024.csv.dvc                 # DVC-managed data / DVC-verwaltete Daten
│   └── kran_wartung_daten.csv                   # Synthetic crane dataset / Synthetischer Kran-Datensatz
├── docs/                                          # Documentation / Dokumentation
│   ├── flight_delay_insights_2024.png           # Flight visualizations / Flug-Visualisierungen
│   ├── crane_maintenance_insights.png           # Crane visualizations / Kran-Visualisierungen
│   └── SQLLITE-INSTALLATION.MD                  # SQLite setup guide / SQLite-Einrichtungsanleitung
├── notebooks/                                     # Jupyter Notebooks
│   ├── flight_delay_prediction_analytics.ipynb  # Flight delay analysis / Flugverspätungs-Analyse
│   └── crane_maintenance_analytics.ipynb        # Crane PdM & RCA analysis / Kran PdM & RCA
├── scripts/                                       # Standalone tools / Eigenständige Skripte
│   └── generate_crane_dataset.py               # Crane dataset generator / Kran-Datensatz-Generator
├── .github/
│   └── COPILOT_INSTRUCTIONS.md                  # Copilot guidelines / Copilot-Richtlinien
├── .gitignore                                     # Git ignore rules / Git ignore Regeln
├── LICENSE                                        # MIT License / MIT-Lizenz
├── README.md                                      # Project documentation / Projektdokumentation
└── requirements.txt                               # Python dependencies / Python Abhängigkeiten
```

---

## 🚀 Quick Start Guide / Schnellstart

> 📖 **Implementation:** [`notebooks/flight_delay_prediction_analytics.ipynb`](notebooks/flight_delay_prediction_analytics.ipynb)  
> 📖 **Installation Guide:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

1. **Clone repository / Repository klonen:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Install dependencies / Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull data (with DVC) / Daten abrufen (mit DVC):**
   ```bash
   dvc pull
   ```

4. **Run notebook / Notebook ausführen:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

---

## 📦 Technology Stack / Technologie-Stack

| Library | Version | Purpose / Zweck |
|---------|---------|-----------------|
| **Python** | 3.13 | Runtime / Laufzeitumgebung |
| **Pandas & NumPy** | latest | Data processing / Datenverarbeitung |
| **Scikit-learn** | latest | Preprocessing and metrics / Preprocessing und Metriken |
| **XGBoost** | latest | ML classifier (`n_estimators=300`, `max_depth=6`, `learning_rate=0.05`) |
| **SQLAlchemy** | latest | Database integration / Datenbankanbindung (`flights2024.db`) |
| **Matplotlib & Seaborn** | latest | Visualization / Visualisierung |
| **DVC** | latest | Data version control / Daten-Versionskontrolle |

> 📖 **Dependencies:** [`requirements.txt`](requirements.txt)

---

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

This project also includes a **synthetic crane drive dataset** generated with `scripts/generate_crane_dataset.py`. It simulates 1,000 hourly sensor readings from a bridge or tower crane hoist unit with injected fault patterns.

*Dieses Projekt enthält außerdem einen **synthetischen Kran-Antriebsdatensatz**, der mit `scripts/generate_crane_dataset.py` erzeugt wird. Er simuliert 1.000 stündliche Sensormesswerte eines Brücken- oder Turmdrehkran-Hubwerks mit eingebetteten Fehlermustern.*

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

---

## 📚 Module and Feature Descriptions / Modul- und Funktionsbeschreibungen

The project includes two complete machine learning pipelines:

*Das Projekt beinhaltet zwei vollständige Machine Learning Pipelines:*

**✈️ Flight Delay Detection**
- Data preprocessing and feature engineering
- Training an XGBoost classifier
- Model evaluation and performance analysis
- Storing predictions in a SQLite database

**🏗️ Crane Predictive Maintenance & RCA**
- Synthetic dataset generation (see `scripts/generate_crane_dataset.py`)
- Root Cause Analysis: XGBoost fault classifier (`Normal` / `E102_Motor_Overheat` / `E505_Bearing_Issue`)
- Predictive Maintenance: Linear regression forecast for brake pad replacement

*✈️ Flugverspätungs-Erkennung*
*- Datenvorverarbeitung und Feature Engineering*
*- Training eines XGBoost Klassifikators*
*- Modell-Evaluation und Leistungsanalyse*
*- Speicherung der Vorhersagen in einer SQLite-Datenbank*

*🏗️ Kran Predictive Maintenance & RCA*
*- Synthetische Datensatzerzeugung (siehe `scripts/generate_crane_dataset.py`)*
*- Root Cause Analysis: XGBoost-Fehlerklassifikator (`Normal` / `E102_Motor_Overheat` / `E505_Bearing_Issue`)*
*- Predictive Maintenance: Lineare Regression zur Vorhersage des Bremsbelag-Austauschs*

---

### ✈️ Flight Delay Detection Pipeline / Flugverspätungs-Erkennungs-Pipeline

#### 1. Data Preparation / Datenaufbereitung

> 📖 **Implementation:** [notebooks/flight_delay_prediction_analytics.ipynb](notebooks/flight_delay_prediction_analytics.ipynb)

Loading flight data from `data/flight_data_2024.csv`  
Creating target variable `Delayed` (1 if `arr_delay > 15`, otherwise 0)  
Storing in SQLite database `flights2024.db`

*Laden der Flugdaten aus `data/flight_data_2024.csv`*  
*Erstellung der Zielvariable `Delayed` (1 wenn `arr_delay > 15`, sonst 0)*  
*Speicherung in SQLite-Datenbank `flights2024.db`*

#### 2. Preprocessing / Vorverarbeitung

Filtering: Only non-cancelled and non-diverted flights  
Label encoding for categorical variables (`op_unique_carrier`, `origin`, `dest`)  
StandardScaler for numeric features  
Train/test split (80/20)

*Filterung: Nur nicht-stornierte und nicht-umgeleitete Flüge*  
*Label-Encoding für kategoriale Variablen (`op_unique_carrier`, `origin`, `dest`)*  
*StandardScaler für numerische Features*  
*Train/Test Split (80/20)*

#### 3. Model Training / Modell-Training

**XGBoost Classifier Hyperparameter:**
- `n_estimators=300`
- `max_depth=6`
- `learning_rate=0.05`

#### 4. Predictions / Vorhersagen

Prediction on full dataset  
Storage in SQLite table `flight_preds_2024`

*Vorhersage auf dem gesamten Datensatz*  
*Speicherung in SQLite-Tabelle `flight_preds_2024`*

### 🏗️ Crane Predictive Maintenance & RCA Pipeline / Kran Predictive Maintenance & RCA Pipeline

> 📖 **Implementation:** [notebooks/crane_maintenance_analytics.ipynb](notebooks/crane_maintenance_analytics.ipynb)

#### 1. Synthetic Dataset Generation / Synthetische Datensatzerzeugung

- Generating 1,000 hourly sensor readings / Erzeugung von 1.000 stündlichen Sensormesswerten
- Injecting fault patterns (`Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue`) / Einbettung von Fehlermustern
- Features: `Load_kg`, `Motor_Temp`, `Vibration`, `Brake_Wear` / Features: Last, Motortemperatur, Vibration, Bremsbelag-Verschleiß

#### 2. Root Cause Analysis (RCA) / Ursachenanalyse

**XGBoost Fault Classifier:**
- Classifying error codes based on sensor patterns / Klassifizierung von Fehlercodes basierend auf Sensormustern
- Identifying whether faults are due to motor overheating or bearing issues / Ermittlung, ob Fehler auf Motorüberhitzung oder Lagerprobleme zurückzuführen sind

#### 3. Predictive Maintenance (PdM) / Vorhersagende Wartung

**Linear Regression Forecast:**
- Predicting brake pad replacement timing / Vorhersage des Zeitpunkts für Bremsbelag-Austausch
- Preventing unexpected downtime / Vermeidung ungeplanter Ausfallzeiten

---

## 🔧 Installation & Setup / Installation und Einrichtung

### Prerequisites / Voraussetzungen

- Python 3.13 or higher / oder höher
- Git
- DVC (for data management / für Datenverwaltung)

### Steps / Schritte

1. **Clone repository / Repository klonen:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Install dependencies / Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull data (with DVC) / Daten abrufen (mit DVC):**
   ```bash
   dvc pull
   ```

4. **Run notebook / Notebook ausführen:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

> 📖 **SQLite Setup:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

---

## 📊 Model Performance / Modell-Performance

| Metric / Metrik | On-Time / Pünktlich (0) | Delayed / Verspätet (1) |
|-----------------|------------------------|------------------------|
| Precision       | 0.94                   | 0.92                   |
| Recall          | 0.98                   | 0.73                   |
| F1-Score        | 0.96                   | 0.81                   |

**Overall Accuracy / Gesamtgenauigkeit: ✅ 93%**

---

## 📌 Next Steps / Nächste Schritte

- [ ] Hyperparameter tuning for better recall on delayed flights  
  *Hyperparameter-Tuning für besseren Recall bei verspäteten Flügen*
- [ ] Feature engineering with weather and airport congestion data  
  *Feature Engineering mit Wetter- und Flughafen-Auslastungsdaten*
- [ ] Deployment as Flask API or Streamlit dashboard  
  *Deployment als Flask API oder Streamlit Dashboard*
- [ ] Integration of additional data sources  
  *Integration zusätzlicher Datenquellen*

---

## 📝 License & Contributions / Lizenz und Beiträge

This project is licensed under the MIT License.

*Dieses Projekt steht unter der MIT-Lizenz.*

> 📖 **License:** [`LICENSE`](LICENSE)