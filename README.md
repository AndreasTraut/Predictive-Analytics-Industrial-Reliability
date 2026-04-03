# 🏭 Prädiktive Analytik für industrielle Zuverlässigkeit v1.0

> **English version:** [README_EN.md](README_EN.md)

Dieses Projekt demonstriert die universelle Anwendbarkeit prädiktiver Analytik über verschiedene Branchen hinweg. Es präsentiert zwei vollständige Machine Learning Pipelines:

**✈️ Flugverspätungs-Vorhersage:** Basierend auf historischen US-Flugdaten von 2024 sagt ein XGBoost-Klassifikator Ankunftsverspätungen mit 93% Genauigkeit voraus. Das Modell analysiert Muster in der Carrier-Performance, Routen und betrieblichen Kennzahlen, um Flüge zu identifizieren, die ein Verspätungsrisiko von über 15 Minuten aufweisen.

**🏗️ Kran Predictive Maintenance & Ursachenanalyse:** Ein synthetischer Datensatz simuliert Sensormesswerte von industriellen Kran-Hubwerken. Die Pipeline kombiniert XGBoost-Klassifikation zur Fehlerdiagnose (`Normal`, `Motor_Overheat`, `Bearing_Issue`) mit linearer Regression zur Vorhersage des Bremsbelag-Austauschzeitpunkts und verhindert so ungeplante Anlagenausfälle. Das erweiterte Notebook [`crane_pdm_enhanced_v2.ipynb`](notebooks/crane_pdm_enhanced_v2.ipynb) ergänzt diese Basis-Pipeline um vier Verbesserungen: Rolling-Feature-Engineering, Bayesianische Hyperparameter-Optimierung mit Optuna, detaillierte Evaluierungsvisualisierungen und Modell-Serialisierung — eingebettet in das **Liebherr LiDAT** Telematik-Framework.

Beide Anwendungsfälle zeigen, wie dieselben Data Science Methoden – Feature Engineering, überwachtes Lernen und Performance-Optimierung – Störungen in komplexen operativen Systemen vorhersagen und verhindern können.

---

## 👨‍💻 Über die Autoren

**Swarada Kulkarni** — Expertin für KI und Analytik, Spezialistin für LLM-Integrationen, Power BI und Python.

🔗 [Vernetze dich auf LinkedIn](https://www.linkedin.com/in/swarada-kulkarni-9ab9571a0/)  
🔗 [Schaue dir weitere Beispiele an](https://github.com/swarada431)

**Andreas Traut** — Senior BI-Entwickler, spezialisiert auf Data Warehousing, SQL Server und Microsoft BI Stack.

🔗 [Vernetze dich auf LinkedIn](https://www.linkedin.com/in/andreas-traut-89340/)  
🔗 [Schaue dir weitere Beispiele an](https://github.com/AndreasTraut)

---

## 📋 Inhaltsverzeichnis

- [🎯 Projektübersicht](#-projektübersicht)
- [📁 Projektstruktur](#-projektstruktur)
- [🚀 Schnellstart](#-schnellstart)
- [📦 Technologie-Stack](#-technologie-stack)
- [📊 Datenquelle](#-datenquelle)
- [📚 Modul- und Funktionsbeschreibungen](#-modul--und-funktionsbeschreibungen)
- [🔧 Installation und Einrichtung](#-installation-und-einrichtung)
- [📊 Modell-Performance](#-modell-performance)
- [📌 Nächste Schritte](#-nächste-schritte)
- [📝 Lizenz und Beiträge](#-lizenz-und-beiträge)

---

## 🎯 Projektübersicht

Dieses Repository zeigt, wie Data Science eingesetzt werden kann, um Störungen in komplexen Systemen vorherzusagen und zu verhindern. Ob ein Flugzeug auf dem Rollfeld verspätet ist oder ein Kran auf einer Baustelle ausfällt – der mathematische Ansatz bleibt derselbe:

- **Luftfahrtlogistik:** Vorhersage von Verspätungen anhand historischer Flugdaten.
- **Ursachenanalyse (RCA):** Ermittlung der Ursache für den Ausfall eines mechanischen Systems (Kran).
- **Predictive Maintenance (PdM):** Schätzung des Servicezeitpunkts einer Komponente, bevor sie ausfällt.

---

## 📁 Projektstruktur

```
Predictive-Analytics-Industrial-Reliability/
├── data/                                          # Datensätze
│   ├── flight_data_2024.csv.dvc                 # DVC-verwaltete Daten
│   └── kran_wartung_daten.csv                   # Synthetischer Kran-Datensatz
├── docs/                                          # Dokumentation
│   ├── flight_delay_insights_2024.png           # Flug-Visualisierungen
│   ├── crane_maintenance_insights.png           # Kran-Visualisierungen
│   └── SQLLITE-INSTALLATION.MD                  # SQLite-Einrichtungsanleitung
├── notebooks/                                     # Jupyter Notebooks
│   ├── flight_delay_prediction_analytics.ipynb  # Flugverspätungs-Analyse
│   ├── crane_maintenance_analytics.ipynb        # Kran PdM & RCA (Basis)
│   └── crane_pdm_enhanced_v2.ipynb              # Kran PdM & RCA (erweitert, LiDAT-Rahmen)
├── scripts/                                       # Eigenständige Skripte
│   └── generate_crane_dataset.py               # Kran-Datensatz-Generator
├── .github/
│   └── COPILOT_INSTRUCTIONS.md                  # Copilot-Richtlinien
├── .gitignore                                     # Git ignore Regeln
├── LICENSE                                        # MIT-Lizenz
├── README.md                                      # Projektdokumentation (Deutsch)
├── README_EN.md                                   # Project documentation (English)
└── requirements.txt                               # Python Abhängigkeiten
```

---

## 🚀 Schnellstart

> 📖 **Implementierung:** [`notebooks/flight_delay_prediction_analytics.ipynb`](notebooks/flight_delay_prediction_analytics.ipynb)  
> 📖 **Installationsanleitung:** [SQLite Installation und Verwendung](docs/SQLLITE-INSTALLATION.MD)

1. **Repository klonen:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Daten abrufen (mit DVC):**
   ```bash
   dvc pull
   ```

4. **Notebook ausführen:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

---

## 📦 Technologie-Stack

| Bibliothek | Version | Zweck |
|------------|---------|-------|
| **Python** | 3.13 | Laufzeitumgebung |
| **Pandas & NumPy** | latest | Datenverarbeitung |
| **Scikit-learn** | latest | Preprocessing und Metriken |
| **XGBoost** | latest | ML-Klassifikator (`n_estimators=300`, `max_depth=6`, `learning_rate=0.05`) |
| **SQLAlchemy** | latest | Datenbankanbindung (`flights2024.db`) |
| **Optuna** | latest | Bayesianische Hyperparameter-Optimierung (TPE) |
| **Matplotlib & Seaborn** | latest | Visualisierung |
| **DVC** | latest | Daten-Versionskontrolle |

> 📖 **Abhängigkeiten:** [`requirements.txt`](requirements.txt)

---

## 📊 Datenquelle

### Flugverspätungs-Datensatz — 2024

Dieses Projekt verwendet den **Flight Delay Dataset — 2024**, der auf Kaggle verfügbar ist.

> 🔗 **Externe Ressource:** [Flight Data 2024 Dataset](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024/data)

### 📥 Download-Details

Es gibt zwei Versionen des Datensatzes:

| Datei | Zeilen | Spalten | Größe | Verwendung |
|-------|--------|---------|-------|------------|
| `flight_data_2024.csv` | ~7 Millionen | 35 | ~1.31 GB | Vollständiger Datensatz |
| `flight_data_2024_sample.csv` | 10,000 | 35 | ~10 MB | Beispieldatensatz für Entwicklung |

### 🔍 Wichtige Features

**Feature Engineering für Verspätungs-Ziel:**
- `DepDel15`: Abflugverspätung > 15 Minuten
- `ArrDel15`: Ankunftsverspätung > 15 Minuten

Diese Spalten können als Basis für die Erstellung der Zielvariable `Delayed` verwendet werden.

### 📌 Ursprung

Die Daten stammen ursprünglich aus der **TranStats On-Time Performance-Datenbank** des US-Verkehrsministeriums (Bureau of Transportation Statistics - BTS).

### 💾 SQLite-Datenbank

Da der vollständige Datensatz über 1 GB groß ist, werden die Vorhersagen in einer SQLite-Datenbank (`flights2024.db`) gespeichert. Dies optimiert die Performance bei Abfragen und ermöglicht effizientes Datenmanagement.

> 📖 **Installationsanleitung:** [SQLite Installation und Verwendung](docs/SQLLITE-INSTALLATION.MD)

---

### 🏗️ Kran-Wartungsdatensatz — Synthetisch

Dieses Projekt enthält außerdem einen **synthetischen Kran-Antriebsdatensatz**, der mit `scripts/generate_crane_dataset.py` erzeugt wird. Er simuliert 1.000 stündliche Sensormesswerte eines Brücken- oder Turmdrehkran-Hubwerks mit eingebetteten Fehlermustern.

> 📖 **Implementierung:** [`scripts/generate_crane_dataset.py`](scripts/generate_crane_dataset.py)  
> 📖 **Analyse-Notebook (Basis):** [`notebooks/crane_maintenance_analytics.ipynb`](notebooks/crane_maintenance_analytics.ipynb)  
> 📖 **Analyse-Notebook (Erweitert):** [`notebooks/crane_pdm_enhanced_v2.ipynb`](notebooks/crane_pdm_enhanced_v2.ipynb)

### 🔍 Kran-Datensatz Features

| Feature | Beschreibung | LiDAT-Konzept | Bedeutung |
|---------|--------------|---------------|----------|
| `Timestamp` | Stündlicher Zeitstempel | Betriebsstunden (Bh) | Zeitachse für Trendanalyse (PdM) |
| `Load_kg` | Aktuelle Last am Haken | Sicherheitsberichte | Überlastung beschleunigt Verschleiß (RCA) |
| `Motor_Temp` | Motortemperatur (°C) | Sensor-Benachrichtigungen | Systematische Überhitzung verkürzt die Isolationslebensdauer (RCA) |
| `Vibration` | Schwingung am Hubwerk (mm/s) | Sensor-Benachrichtigungen | RCA: Hohe Werte deuten auf Lager-/Getriebedefekt hin |
| `Brake_Wear` | Verbleibende Belagdicke (mm) | Nutzungstrends | Direktes Verschleißmaß (PdM) |
| `Error_Code` | Fehlerbezeichnung (Zielvariable) | Teleservice-Fehlerprotokoll | `Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue` |

### 🚀 Datensatz neu erzeugen

```bash
python scripts/generate_crane_dataset.py
```

---

## 📚 Modul- und Funktionsbeschreibungen

Das Projekt beinhaltet zwei vollständige Machine Learning Pipelines:

**✈️ Flugverspätungs-Erkennung**
- Datenvorverarbeitung und Feature Engineering
- Training eines XGBoost Klassifikators
- Modell-Evaluation und Leistungsanalyse
- Speicherung der Vorhersagen in einer SQLite-Datenbank

**🏗️ Kran Predictive Maintenance & RCA**
- Synthetische Datensatzerzeugung (siehe `scripts/generate_crane_dataset.py`)
- Root Cause Analysis: XGBoost-Fehlerklassifikator (`Normal` / `E102_Motor_Overheat` / `E505_Bearing_Issue`)
- Predictive Maintenance: Lineare Regression zur Vorhersage des Bremsbelag-Austauschs

**🏗️ Kran PdM & RCA — Erweiterte Pipeline (LiDAT-Rahmen)**
- Vollständig selbstenthaltendes Notebook mit 2.000 synthetischen Sensormesswerten
- Framing nach dem **Liebherr LiDAT** Telematik-System (Safety Reports, Sensor Notifications, Teleservice, Operating Hours, Usage Trends)
- Rolling-Feature-Engineering: 12-h- und 24-h-Gleitfenster-Statistiken (Mittelwert, Std, Min, Max) pro Sensor
- Bayesianische Hyperparameter-Optimierung mit **Optuna** (Tree-structured Parzen Estimator, TPE)
- Chronologischer 80/20-Split (kein Shuffling) für zeitreihenkonforme Auswertung
- Umfangreiche Evaluierungsvisualisierungen: normalisierte Konfusionsmatrix, klassen-spezifische F1-Balkendiagramme, One-vs-Rest ROC-Kurven, Feature-Importance-Diagramme
- Modell-Serialisierung via `joblib`: vollständiges Inferenz-Bundle (Scaler + Klassifikator + Label-Encoder)

---

### ✈️ Flugverspätungs-Erkennungs-Pipeline

#### 1. Datenaufbereitung

> 📖 **Implementierung:** [notebooks/flight_delay_prediction_analytics.ipynb](notebooks/flight_delay_prediction_analytics.ipynb)

Laden der Flugdaten aus `data/flight_data_2024.csv`  
Erstellung der Zielvariable `Delayed` (1 wenn `arr_delay > 15`, sonst 0)  
Speicherung in SQLite-Datenbank `flights2024.db`

#### 2. Vorverarbeitung

Filterung: Nur nicht-stornierte und nicht-umgeleitete Flüge  
Label-Encoding für kategoriale Variablen (`op_unique_carrier`, `origin`, `dest`)  
StandardScaler für numerische Features  
Train/Test Split (80/20)

#### 3. Modell-Training

**XGBoost Classifier Hyperparameter:**
- `n_estimators=300`
- `max_depth=6`
- `learning_rate=0.05`

#### 4. Vorhersagen

Vorhersage auf dem gesamten Datensatz  
Speicherung in SQLite-Tabelle `flight_preds_2024`

### 🏗️ Kran Predictive Maintenance & RCA Pipeline

> 📖 **Implementierung (Basis):** [notebooks/crane_maintenance_analytics.ipynb](notebooks/crane_maintenance_analytics.ipynb)  
> 📖 **Implementierung (Erweitert):** [notebooks/crane_pdm_enhanced_v2.ipynb](notebooks/crane_pdm_enhanced_v2.ipynb)

#### 1. Synthetische Datensatzerzeugung

- Erzeugung von 1.000 stündlichen Sensormesswerten (2.000 im erweiterten Notebook)
- Einbettung von Fehlermustern (`Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue`)
- Features: Last, Motortemperatur, Vibration, Bremsbelag-Verschleiß

#### 2. Ursachenanalyse — Story A (RCA)

**LiDAT-Äquivalent:** Safety Reports + Sensor Notifications + Teleservice Ferndiagnose.

**XGBoost-Fehlerklassifikator:**
- Klassifizierung von Fehlercodes basierend auf Sensormustern
- Ermittlung, ob Fehler auf Motorüberhitzung oder Lagerprobleme zurückzuführen sind

**Besonderheiten des erweiterten Notebooks:**

| # | Modul | Beschreibung |
|---|-------|-------------|
| 1 | **Rolling-Feature-Engineering** | 12-h- und 24-h-Gleitfenster (Mittelwert, Std, Min, Max) erfassen zeitliche Degradationssignale vor einem Fehler |
| 2 | **Hyperparameter-Tuning mit Optuna** | Bayesianische Suche (TPE) über `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree`, `min_child_weight` |
| 3 | **Chronologischer Split** | 80/20-Aufteilung ohne Shuffling — respektiert die Zeitreihennatur der Daten |
| 4 | **Evaluierungsvisualisierungen** | Normalisierte Konfusionsmatrix, klassen-spezifisches F1-Diagramm, One-vs-Rest ROC-Kurven, Top-20 Feature-Importances |

#### 3. Vorhersagende Wartung — Story B (PdM)

**LiDAT-Äquivalent:** Betriebsstunden (Bh) + Nutzungstrends + Verfügbarkeitsplanung.

**Lineare Regression Vorhersage:**
- Vorhersage des Zeitpunkts für Bremsbelag-Austausch (Unterschreitung der kritischen Schwelle von 1,0 mm)
- Vermeidung ungeplanter Ausfallzeiten

#### 4. Modell-Serialisierung

Gespeicherte Artefakte (erweiterte Pipeline):
- `outputs/crane_rca_pipeline.joblib` — vollständiges RCA-Inferenz-Bundle (Scaler + Klassifikator + Label-Encoder)
- `outputs/crane_pdm_regression.joblib` — PdM Lineare-Regression-Modell
- `outputs/feature_cols.txt` — sortierte Feature-Liste für Column-Alignment

---

## 🔧 Installation und Einrichtung

### Voraussetzungen

- Python 3.13 oder höher
- Git
- DVC (für Datenverwaltung)

### Schritte

1. **Repository klonen:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Daten abrufen (mit DVC):**
   ```bash
   dvc pull
   ```

4. **Notebook ausführen:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

> 📖 **SQLite Setup:** [SQLite Installation und Verwendung](docs/SQLLITE-INSTALLATION.MD)

---

## 📊 Modell-Performance

| Metrik | Pünktlich (0) | Verspätet (1) |
|--------|--------------|---------------|
| Precision | 0.94 | 0.92 |
| Recall | 0.98 | 0.73 |
| F1-Score | 0.96 | 0.81 |

**Gesamtgenauigkeit: ✅ 93%**

---

## 📌 Nächste Schritte

- [ ] Hyperparameter-Tuning für besseren Recall bei verspäteten Flügen
- [ ] Feature Engineering mit Wetter- und Flughafen-Auslastungsdaten
- [ ] Deployment als Flask API oder Streamlit Dashboard
- [ ] Integration zusätzlicher Datenquellen
- [ ] **SHAP** — `shap.TreeExplainer` für per-Vorhersage-Erklärungen im RCA-Modell
- [ ] **Drift-Erkennung** — Überwachung der Rolling-Feature-Verteilungen in der Produktion mit `evidently`
- [ ] **MLflow** — Ersatz der `joblib`-Bundles durch `mlflow.xgboost.log_model` für Experiment-Versionierung
- [ ] **Nicht-lineares PdM** — Ersatz der linearen Regression durch ein exponentielles oder polynomiales Verschleißmodell
- [ ] **Lastgewichteter Verschleiß** — Gewichtung der Bremsbelag-Verschleißrate nach `Load_kg` pro Zyklus

---

## 📝 Lizenz und Beiträge

Dieses Projekt steht unter der MIT-Lizenz.

> 📖 **Lizenz:** [`LICENSE`](LICENSE)