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


<img width="1919" height="630" alt="Screenshot 2026-06-17 191637" src="https://github.com/user-attachments/assets/105005ed-2176-45d7-b506-2936672def60" />
<img width="1919" height="523" alt="Screenshot 2026-06-17 191917" src="https://github.com/user-attachments/assets/89aac550-4191-434e-813f-204e2a9bb719" />
<img width="1919" height="901" alt="Screenshot 2026-06-17 191854" src="https://github.com/user-attachments/assets/37b272c6-4a11-4691-a526-ec5fb1667edd" />
<img width="1915" height="568" alt="Screenshot 2026-06-17 191833" src="https://github.com/user-attachments/assets/f8f7b361-a4d1-47eb-8244-5a72159d8be5" />
<img width="1918" height="646" alt="Screenshot 2026-06-17 191809" src="https://github.com/user-attachments/assets/f517f833-7134-4fa7-b8bf-9769556ecb9d" />
<img width="1919" height="595" alt="Screenshot 2026-06-17 191701" src="https://github.com/user-attachments/assets/8a1642c1-ba3f-4748-9cbf-ec2821e8f770" />






