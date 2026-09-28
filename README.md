<div align="center">

# 🏏 Cricket AI

### AI-Powered Cricket Analytics & Prediction Platform

**Turning historical cricket data into predictions, performance insights and interactive analytics.**

`Python` • `Streamlit` • `XGBoost` • `Pandas` • `Plotly` • `Scikit-Learn`

</div>

---

## 🚀 Overview

**Cricket AI** is an end-to-end cricket analytics platform built using Python, Machine Learning and Streamlit.

The project processes historical cricket match data to provide **AI-powered win predictions, batting and bowling analytics, venue insights, team performance analysis and interactive visualizations** through an easy-to-use dashboard.

The system combines data preprocessing, feature engineering, machine learning and interactive analytics in one application.

---

## ✨ Key Features

🏆 **AI Win Prediction** — Predict match outcomes using an XGBoost classification model

🏏 **Batting Analytics** — Explore batting performance from historical match data

🎯 **Bowling Analytics** — Analyze bowling performance and statistics

🏟️ **Venue Insights** — Understand match patterns across different venues

📊 **Team Performance Analysis** — Compare and explore team-level performance

📈 **Interactive Visualizations** — Explore cricket data through Plotly charts

🖥️ **Streamlit Dashboard** — Access predictions and analytics through an interactive interface

---

## 🧠 Machine Learning Pipeline

```text
Historical Match Data
        │
        ▼
Data Preprocessing
   Pandas / Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
 XGBoost Classifier
        │
        ▼
   Trained Model
        │
        ▼
 AI Win Prediction
```

The analytics pipeline works alongside the ML model to transform historical match data into dashboard insights and visualizations.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │ Historical JSON Data│
                    │    1200+ Matches    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    │       Pandas        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Cleaned Dataset    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
             ▼                                   ▼
   ┌─────────────────────┐             ┌─────────────────────┐
   │ Feature Engineering │             │  Analytics Engine   │
   └──────────┬──────────┘             │   Pandas + Plotly   │
              │                        └──────────┬──────────┘
              ▼                                   │
   ┌─────────────────────┐                        ▼
   │ XGBoost Classifier  │             ┌─────────────────────┐
   │   Model Training    │             │ Dashboard Insights  │
   └──────────┬──────────┘             └──────────┬──────────┘
              │                                   │
              └─────────────────┬─────────────────┘
                                │
                                ▼
                    ┌─────────────────────┐
                    │ Streamlit Dashboard │
                    │                     │
                    │ • Team Filters      │
                    │ • Venue Filters     │
                    │ • Win Predictor     │
                    │ • Analytics         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   End User          │
                    │ Interactive Insights│
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Dashboard | Streamlit |
| Machine Learning | XGBoost, Scikit-Learn |
| Data Processing | Pandas |
| Visualization | Plotly |
| Model Persistence | Joblib |
| Data | Historical cricket match data |

---

## 📊 Dashboard Preview

### Cricket Analytics Dashboard

<img width="100%" alt="Cricket AI Dashboard" src="https://github.com/user-attachments/assets/105005ed-2176-45d7-b506-2936672def60" />

### Match & Performance Analytics

<img width="100%" alt="Cricket Match Analytics" src="https://github.com/user-attachments/assets/89aac550-4191-434e-813f-204e2a9bb719" />

<img width="100%" alt="Cricket Performance Analytics" src="https://github.com/user-attachments/assets/37b272c6-4a11-4691-a526-ec5fb1667edd" />

### Player & Venue Insights

<img width="100%" alt="Cricket Player Analytics" src="https://github.com/user-attachments/assets/f8f7b361-a4d1-47eb-8244-5a72159d8be5" />

<img width="100%" alt="Cricket Venue Analytics" src="https://github.com/user-attachments/assets/f517f833-7134-4fa7-b8bf-9769556ecb9d" />

### AI Prediction

<img width="100%" alt="Cricket AI Prediction" src="https://github.com/user-attachments/assets/8a1642c1-ba3f-4748-9cbf-ec2821e8f770" />

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Adithya200116/Cricket_AI-.git
cd Cricket_AI-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit application

```bash
streamlit run dashboard.py
```

Then open the local Streamlit URL displayed in your terminal.

---

## 🎯 Project Highlights

This project demonstrates practical experience with:

- End-to-end machine learning workflows
- Data cleaning and preprocessing
- Feature engineering
- XGBoost classification
- Sports and performance analytics
- Interactive data visualization
- Streamlit application development
- Converting raw historical data into usable insights

---

<div align="center">

### 🏏 Data → Machine Learning → Cricket Intelligence

**Built by Adithya M Kaushik**

</div>
