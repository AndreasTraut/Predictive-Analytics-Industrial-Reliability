# 🏭 Predictive Analytics for Industrial Reliability v1.0

This project demonstrates the universal applicability of predictive analytics across diverse industries. It showcases two complete machine learning pipelines:

**✈️ Flight Delay Prediction:** Using historical U.S. flight data from 2024, an XGBoost classifier predicts arrival delays with 93% accuracy. The model analyzes patterns in carrier performance, routes, and operational metrics to identify flights at risk of delays greater than 15 minutes.

**🏗️ Crane Predictive Maintenance & Root Cause Analysis:** A synthetic dataset simulates sensor readings from industrial crane hoist systems. The pipeline combines XGBoost classification for fault diagnosis (`Normal`, `Motor_Overheat`, `Bearing_Issue`) with linear regression to forecast brake pad replacement timing, preventing unexpected equipment downtime. The enhanced notebook [`crane_pdm_enhanced_v2.ipynb`](notebooks/crane_pdm_enhanced_v2.ipynb) extends this baseline pipeline with four improvements: rolling feature engineering, Bayesian hyperparameter optimisation with Optuna, detailed evaluation visuals, and model serialisation — all framed within the **Liebherr LiDAT** telematics system.

Both use cases demonstrate how the same data science methodologies—feature engineering, supervised learning, and performance optimization—can predict and prevent disruptions in complex operational systems.

---

## 👨‍💻 About the Authors

**Swarada Kulkarni** — AI & Analytics Professional, expert on LLM Integrations, Power BI and Python.

🔗 [Connect on LinkedIn](https://www.linkedin.com/in/swarada-kulkarni-9ab9571a0/)  
🔗 [Have a look at more examples](https://github.com/swarada431)

**Andreas Traut** — Senior BI developer specializing in data warehousing, SQL Server, and Microsoft BI Stack.

🔗 [Connect on LinkedIn](https://www.linkedin.com/in/andreas-traut-89340/)  
🔗 [Have a look at more examples](https://github.com/AndreasTraut)

---

## 📋 Table of Contents

- [🎯 Repository Overview](#-repository-overview)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start Guide](#-quick-start-guide)
- [📦 Technology Stack](#-technology-stack)
- [📊 Data Source](#-data-source)
- [📚 Module and Feature Descriptions](#-module-and-feature-descriptions)
- [🔧 Installation & Setup](#-installation--setup)
- [📊 Model Performance](#-model-performance)
- [📌 Next Steps](#-next-steps)
- [📝 License & Contributions](#-license--contributions)

---

## 🎯 Repository Overview

This repository demonstrates how data science can be used to predict and prevent disruptions in complex systems. Whether it's a plane delayed on the tarmac or a crane failing on a construction site, the mathematical approach remains the same:

- **Aviation Logistics:** Predicting delays using historical flight data.
- **Root Cause Analysis (RCA):** Identifying why a mechanical system (crane) failed.
- **Predictive Maintenance (PdM):** Estimating when a component needs service before it breaks.

---

## 📁 Project Structure

```
Predictive-Analytics-Industrial-Reliability/
├── data/                                          # Datasets
│   ├── flight_data_2024.csv.dvc                 # DVC-managed data
│   └── kran_wartung_daten.csv                   # Synthetic crane dataset
├── docs/                                          # Documentation
│   ├── flight_delay_insights_2024.png           # Flight visualizations
│   ├── crane_maintenance_insights.png           # Crane visualizations
│   └── SQLLITE-INSTALLATION.MD                  # SQLite setup guide
├── notebooks/                                     # Jupyter Notebooks
│   ├── flight_delay_prediction_analytics.ipynb  # Flight delay analysis
│   ├── crane_maintenance_analytics.ipynb        # Crane PdM & RCA (baseline)
│   └── crane_pdm_enhanced_v2.ipynb              # Crane PdM & RCA (enhanced, LiDAT framing)
├── scripts/                                       # Standalone tools
│   └── generate_crane_dataset.py               # Crane dataset generator
├── .github/
│   └── COPILOT_INSTRUCTIONS.md                  # Copilot guidelines
├── .gitignore                                     # Git ignore rules
├── LICENSE                                        # MIT License
├── README.md                                      # Project documentation (German)
├── README_EN.md                                   # Project documentation (English)
└── requirements.txt                               # Python dependencies
```

---

## 🚀 Quick Start Guide

> 📖 **Implementation:** [`notebooks/flight_delay_prediction_analytics.ipynb`](notebooks/flight_delay_prediction_analytics.ipynb)  
> 📖 **Installation Guide:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

1. **Clone repository:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull data (with DVC):**
   ```bash
   dvc pull
   ```

4. **Run notebook:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

---

## 📦 Technology Stack

| Library | Version | Purpose |
|---------|---------|---------|
| **Python** | 3.13 | Runtime |
| **Pandas & NumPy** | latest | Data processing |
| **Scikit-learn** | latest | Preprocessing and metrics |
| **XGBoost** | latest | ML classifier (`n_estimators=300`, `max_depth=6`, `learning_rate=0.05`) |
| **SQLAlchemy** | latest | Database integration (`flights2024.db`) |
| **Optuna** | latest | Bayesian hyperparameter optimisation (TPE) |
| **Matplotlib & Seaborn** | latest | Visualization |
| **DVC** | latest | Data version control |

> 📖 **Dependencies:** [`requirements.txt`](requirements.txt)

---

## 📊 Data Source

### Flight Delay Dataset — 2024

This project uses the **Flight Delay Dataset — 2024**, available on Kaggle.

> 🔗 **External Resource:** [Flight Data 2024 Dataset](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024/data)

### 📥 Download Details

There are two versions of the dataset:

| File | Rows | Columns | Size | Usage |
|------|------|---------|------|-------|
| `flight_data_2024.csv` | ~7 million | 35 | ~1.31 GB | Full dataset |
| `flight_data_2024_sample.csv` | 10,000 | 35 | ~10 MB | Sample for development |

### 🔍 Key Features

**Feature Engineering for Delay Target:**
- `DepDel15`: Departure delay > 15 minutes
- `ArrDel15`: Arrival delay > 15 minutes

These columns can be used as the basis for creating the `Delayed` target variable.

### 📌 Original Source

The data originally comes from the **TranStats On-Time Performance database** of the U.S. Department of Transportation (Bureau of Transportation Statistics - BTS).

### 💾 SQLite Database

Since the full dataset is over 1 GB, predictions are stored in a SQLite database (`flights2024.db`). This optimizes query performance and enables efficient data management.

> 📖 **Installation Guide:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

---

### 🏗️ Crane Maintenance Dataset — Synthetic

This project also includes a **synthetic crane drive dataset** generated with `scripts/generate_crane_dataset.py`. It simulates 1,000 hourly sensor readings from a bridge or tower crane hoist unit with injected fault patterns.

> 📖 **Implementation:** [`scripts/generate_crane_dataset.py`](scripts/generate_crane_dataset.py)  
> 📖 **Analysis Notebook (baseline):** [`notebooks/crane_maintenance_analytics.ipynb`](notebooks/crane_maintenance_analytics.ipynb)  
> 📖 **Analysis Notebook (enhanced):** [`notebooks/crane_pdm_enhanced_v2.ipynb`](notebooks/crane_pdm_enhanced_v2.ipynb)

### 🔍 Crane Dataset Features

| Feature | Description | LiDAT Concept | Relevance |
|---------|-------------|---------------|-----------|
| `Timestamp` | Hourly observation timestamp | Operating Hours (Bh) | Time axis for trend analysis (PdM) |
| `Load_kg` | Current hook load | Safety Reports | Overload accelerates wear (RCA) |
| `Motor_Temp` | Hoist motor temperature (°C) | Sensor Notifications | Systematic overheating shortens insulation life (RCA) |
| `Vibration` | Vibration at hoist unit (mm/s) | Sensor Notifications | RCA: high values indicate bearing/gearbox fault |
| `Brake_Wear` | Remaining brake pad thickness (mm) | Usage Trends | Direct wear measure (PdM) |
| `Error_Code` | Fault label (target variable) | Teleservice fault log | `Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue` |

### 🚀 Regenerate the Dataset

```bash
python scripts/generate_crane_dataset.py
```

---

## 📚 Module and Feature Descriptions

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

**🏗️ Crane PdM & RCA — Enhanced Pipeline (LiDAT Framing)**
- Fully self-contained notebook with 2,000 synthetic sensor readings
- Framed around the **Liebherr LiDAT** telematics system (Safety Reports, Sensor Notifications, Teleservice, Operating Hours, Usage Trends)
- Rolling feature engineering: 12-h and 24-h sliding-window statistics (mean, std, min, max) per sensor
- Bayesian hyperparameter optimisation with **Optuna** (Tree-structured Parzen Estimator, TPE)
- Chronological 80/20 split (no shuffling) for time-series-compliant evaluation
- Comprehensive evaluation visuals: normalised confusion matrix, per-class F1 bar chart, One-vs-Rest ROC curves, feature importance plots
- Model serialisation via `joblib`: full inference bundle (scaler + classifier + label encoder)

---

### ✈️ Flight Delay Detection Pipeline

#### 1. Data Preparation

> 📖 **Implementation:** [notebooks/flight_delay_prediction_analytics.ipynb](notebooks/flight_delay_prediction_analytics.ipynb)

Loading flight data from `data/flight_data_2024.csv`  
Creating target variable `Delayed` (1 if `arr_delay > 15`, otherwise 0)  
Storing in SQLite database `flights2024.db`

#### 2. Preprocessing

Filtering: Only non-cancelled and non-diverted flights  
Label encoding for categorical variables (`op_unique_carrier`, `origin`, `dest`)  
StandardScaler for numeric features  
Train/test split (80/20)

#### 3. Model Training

**XGBoost Classifier Hyperparameter:**
- `n_estimators=300`
- `max_depth=6`
- `learning_rate=0.05`

#### 4. Predictions

Prediction on full dataset  
Storage in SQLite table `flight_preds_2024`

### 🏗️ Crane Predictive Maintenance & RCA Pipeline

> 📖 **Implementation (baseline):** [notebooks/crane_maintenance_analytics.ipynb](notebooks/crane_maintenance_analytics.ipynb)  
> 📖 **Implementation (enhanced):** [notebooks/crane_pdm_enhanced_v2.ipynb](notebooks/crane_pdm_enhanced_v2.ipynb)

#### 1. Synthetic Dataset Generation

- Generating 1,000 hourly sensor readings (2,000 in the enhanced notebook)
- Injecting fault patterns (`Normal`, `E102_Motor_Overheat`, `E505_Bearing_Issue`)
- Features: `Load_kg`, `Motor_Temp`, `Vibration`, `Brake_Wear`

#### 2. Root Cause Analysis — Story A (RCA)

**LiDAT equivalent:** Safety Reports + Sensor Notifications + Teleservice remote diagnosis.

**XGBoost Fault Classifier:**
- Classifying error codes based on sensor patterns
- Identifying whether faults are due to motor overheating or bearing issues

**Highlights of the enhanced notebook:**

| # | Module | Description |
|---|--------|-------------|
| 1 | **Rolling feature engineering** | 12-h and 24-h sliding windows (mean, std, min, max) capture temporal degradation signals before a fault |
| 2 | **Hyperparameter tuning with Optuna** | Bayesian search (TPE) over `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree`, `min_child_weight` |
| 3 | **Chronological split** | 80/20 split without shuffling — respects the time-series nature of the data |
| 4 | **Evaluation visuals** | Normalised confusion matrix, per-class F1 bar chart, One-vs-Rest ROC curves, Top-20 feature importances |

#### 3. Predictive Maintenance — Story B (PdM)

**LiDAT equivalent:** Operating Hours (Bh) tracking + Usage Trends + Availability planning.

**Linear Regression Forecast:**
- Predicting brake pad replacement timing (crossing the critical threshold of 1.0 mm)
- Preventing unexpected downtime

#### 4. Model Serialisation

Saved artefacts (enhanced pipeline):
- `outputs/crane_rca_pipeline.joblib` — full RCA inference bundle (scaler + classifier + label encoder)
- `outputs/crane_pdm_regression.joblib` — PdM linear regression model
- `outputs/feature_cols.txt` — ordered feature list for column alignment

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.13 or higher
- Git
- DVC (for data management)

### Steps

1. **Clone repository:**
   ```bash
   git clone https://github.com/AndreasTraut/Predictive-Analytics-Industrial-Reliability.git
   cd Predictive-Analytics-Industrial-Reliability
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull data (with DVC):**
   ```bash
   dvc pull
   ```

4. **Run notebook:**
   ```bash
   jupyter notebook notebooks/flight_delay_prediction_analytics.ipynb
   ```

> 📖 **SQLite Setup:** [SQLite Installation and Usage](docs/SQLLITE-INSTALLATION.MD)

---

## 📊 Model Performance

| Metric | On-Time (0) | Delayed (1) |
|--------|-------------|-------------|
| Precision | 0.94 | 0.92 |
| Recall | 0.98 | 0.73 |
| F1-Score | 0.96 | 0.81 |

**Overall Accuracy: ✅ 93%**

---

## 📌 Next Steps

- [ ] Hyperparameter tuning for better recall on delayed flights
- [ ] Feature engineering with weather and airport congestion data
- [ ] Deployment as Flask API or Streamlit dashboard
- [ ] Integration of additional data sources
- [ ] **SHAP** — add `shap.TreeExplainer` for per-prediction explanations on the RCA model
- [ ] **Drift detection** — monitor rolling feature distributions in production with `evidently`
- [ ] **MLflow** — replace `joblib` bundles with `mlflow.xgboost.log_model` for experiment versioning
- [ ] **Non-linear PdM** — replace linear regression with an exponential or polynomial decay model for more realistic brake wear curves
- [ ] **Load-weighted degradation** — weight brake wear rate by `Load_kg` per cycle, not just time

---

## 📝 License & Contributions

This project is licensed under the MIT License.

> 📖 **License:** [`LICENSE`](LICENSE)
