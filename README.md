# Cricket AI Analytics Dashboard

🏏 Cricket AI Analytics Dashboard built using Python, Streamlit, XGBoost, and Machine Learning. The project provides AI-powered win prediction, batting and bowling analytics, venue insights, team performance analysis, and interactive visualizations using historical cricket match data.

## Features
- AI Win Prediction
- Batting Analytics
- Bowling Analytics
- Venue Insights
- Team Performance Analysis
- Interactive Visualizations
- Streamlit Dashboard

## Tech Stack
- Python
- Streamlit
- XGBoost
- Pandas
- Plotly
- Scikit-Learn

## Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py



                         ┌─────────────────────┐
                         │   Raw JSON Files    │
                         │   (1200+ Matches)   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Preprocessing  │
                         │ Pandas / Cleaning   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ cleaned_matches.csv │
                         └──────────┬──────────┘
                                    │
               ┌────────────────────┴────────────────────┐
               │                                         │
               ▼                                         ▼
    ┌─────────────────────┐                ┌─────────────────────┐
    │ Feature Engineering │                │ Analytics Engine    │
    │                     │                │ Pandas + Plotly     │
    └──────────┬──────────┘                └──────────┬──────────┘
               │                                      │
               ▼                                      ▼
    ┌─────────────────────┐                ┌─────────────────────┐
    │ XGBoost Classifier  │                │ Dashboard Insights  │
    │ Model Training      │                │ KPI & Visualizations│
    └──────────┬──────────┘                └──────────┬──────────┘
               │                                      │
               ▼                                      ▼
    ┌─────────────────────┐                ┌─────────────────────┐
    │ cricket_ai_model.pkl│                │ Plotly Charts       │
    └──────────┬──────────┘                │ • Top Batters       │
               │                           │ • Top Bowlers       │
               │                           │ • Venue Analysis    │
               │                           │ • Run Rate Trends   │
               │                           └──────────┬──────────┘
               │                                      │
               └──────────────────┬───────────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │   Streamlit Dashboard   │
                     │                         │
                     │ • Team Filters          │
                     │ • Venue Filters         │
                     │ • AI Win Predictor      │
                     │ • Analytics Dashboard   │
                     └───────────┬─────────────┘
                                 │
                                 ▼
                     ┌─────────────────────────┐
                     │   End User Interface    │
                     │   Real-Time Insights    │
                     └─────────────────────────┘


Tech Stack Diagram

┌─────────────┐
│ JSON Files  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Pandas    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  XGBoost    │
│ ML Model    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Joblib    │
│ Model Save  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Streamlit   │
│ Dashboard   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Plotly    │
│ Visuals     │
└─────────────┘
