import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Cricket AI Dashboard",
    page_icon="🏏",
    layout="wide"
)

# =========================================
# LOAD DATA
# =========================================

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_matches.csv")

df = load_data()

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load("models/cricket_ai_model.pkl")

# =========================================
# TITLE
# =========================================

st.title("🏏 Cricket AI Analytics Dashboard")

st.markdown("""
### Real-Time Cricket Intelligence System

Features:
- AI Win Prediction
- Batting Analytics
- Bowling Analytics
- Venue Insights
- Team Performance Analysis
""")

st.markdown("---")

# =========================================
# SIDEBAR FILTERS
# =========================================

st.sidebar.header("Filters")

teams = ["All"] + sorted(
    df["batting_team"].dropna().unique().tolist()
)

selected_team = st.sidebar.selectbox(
    "Select Team",
    teams
)

venues = ["All"] + sorted(
    df["venue"].dropna().astype(str).unique().tolist()
)

selected_venue = st.sidebar.selectbox(
    "Select Venue",
    venues
)

# =========================================
# FILTER DATA
# =========================================

filtered_df = df.copy()

if selected_team != "All":
    filtered_df = filtered_df[
        filtered_df["batting_team"] == selected_team
    ]

if selected_venue != "All":
    filtered_df = filtered_df[
        filtered_df["venue"].astype(str) == selected_venue
    ]

# =========================================
# KPI SECTION
# =========================================

total_runs = int(filtered_df["total_runs"].sum())

total_wickets = int(filtered_df["wicket"].sum())

matches = filtered_df["match_id"].nunique()

avg_rr = round(
    filtered_df["current_run_rate"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("🏏 Total Runs", total_runs)

col2.metric("🎯 Total Wickets", total_wickets)

col3.metric("📅 Matches", matches)

col4.metric("⚡ Avg Run Rate", avg_rr)

st.markdown("---")

# =========================================
# TOP BATTERS
# =========================================

st.subheader("🔥 Top Run Scorers")

top_batters = (
    filtered_df.groupby("batter")["batter_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_batters,
    x="batter",
    y="batter_runs",
    title="Top 10 Run Scorers",
    text_auto=True
)

st.plotly_chart(fig1, use_container_width=True)

# =========================================
# TOP BOWLERS
# =========================================

st.subheader("🎯 Top Wicket Takers")

top_bowlers = (
    filtered_df[filtered_df["wicket"] == 1]
    .groupby("bowler")
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index(name="wickets")
)

fig2 = px.bar(
    top_bowlers,
    x="bowler",
    y="wickets",
    title="Top Wicket Takers",
    text_auto=True
)

st.plotly_chart(fig2, use_container_width=True)

# =========================================
# RUN RATE ANALYSIS
# =========================================

st.subheader("📈 Run Rate Analysis")

runrate_df = (
    filtered_df.groupby("over")["total_runs"]
    .mean()
    .reset_index()
)

fig3 = px.line(
    runrate_df,
    x="over",
    y="total_runs",
    markers=True,
    title="Average Runs Per Over"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================================
# VENUE ANALYSIS
# =========================================

st.subheader("🏟️ Best Batting Venues")

venue_stats = (
    filtered_df.groupby("venue")["total_runs"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    venue_stats,
    x="venue",
    y="total_runs",
    title="Highest Scoring Venues",
    text_auto=True
)

st.plotly_chart(fig4, use_container_width=True)

# =========================================
# TEAM RUN DISTRIBUTION
# =========================================

st.subheader("🏆 Team Run Distribution")

team_stats = (
    filtered_df.groupby("batting_team")["total_runs"]
    .sum()
    .reset_index()
)

fig5 = px.pie(
    team_stats,
    names="batting_team",
    values="total_runs",
    title="Run Distribution"
)

st.plotly_chart(fig5, use_container_width=True)

# =========================================
# LIVE AI WIN PREDICTOR
# =========================================

st.markdown("---")

st.header("🤖 Live AI Win Predictor")

col1, col2 = st.columns(2)

with col1:

    innings = st.selectbox(
        "Innings",
        [1, 2]
    )

    over = st.number_input(
        "Current Over",
        min_value=0.0,
        max_value=20.0,
        value=15.0,
        step=0.1
    )

    score = st.number_input(
        "Current Score",
        min_value=0,
        max_value=400,
        value=150
    )

    wickets = st.number_input(
        "Wickets Fallen",
        min_value=0,
        max_value=10,
        value=3
    )

with col2:

    run_rate = st.number_input(
        "Current Run Rate",
        min_value=0.0,
        max_value=20.0,
        value=8.0,
        step=0.1
    )

    target_runs = st.number_input(
        "Target Runs",
        min_value=0,
        max_value=500,
        value=180
    )

    balls_remaining = st.number_input(
        "Balls Remaining",
        min_value=0,
        max_value=120,
        value=24
    )

    required_run_rate = st.number_input(
        "Required Run Rate",
        min_value=0.0,
        max_value=36.0,
        value=7.5,
        step=0.1
    )

# =========================================
# MODEL PREDICTION
# =========================================

live_data = pd.DataFrame({
    "innings": [innings],
    "over": [over],
    "cumulative_score": [score],
    "wickets_fallen": [wickets],
    "current_run_rate": [run_rate],
    "target_runs": [target_runs],
    "balls_remaining": [balls_remaining],
    "required_run_rate": [required_run_rate]
})

prediction = model.predict_proba(live_data)

win_probability = prediction[0][1] * 100
lose_probability = prediction[0][0] * 100

# =========================================
# RESULT
# =========================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🏆 Win Probability",
        f"{win_probability:.2f}%"
    )

with col2:
    st.metric(
        "❌ Lose Probability",
        f"{lose_probability:.2f}%"
    )

st.progress(int(win_probability))

# =========================================
# AI INSIGHT
# =========================================

st.subheader("🎙️ AI Match Insight")

if win_probability > 80:

    st.success(
        "🔥 Dominating position. The batting side is highly likely to win."
    )

elif win_probability > 60:

    st.info(
        "💪 Strong advantage to the batting team."
    )

elif win_probability > 40:

    st.warning(
        "⚖️ Balanced contest. The next few overs are crucial."
    )

else:

    st.error(
        "🎯 Bowling side currently has the advantage."
    )

# =========================================
# MODEL PREDICTION
# =========================================

live_data = pd.DataFrame({
    "innings": [innings],
    "over": [over],
    "cumulative_score": [score],
    "wickets_fallen": [wickets],
    "current_run_rate": [run_rate],
    "target_runs": [target_runs],
    "balls_remaining": [balls_remaining],
    "required_run_rate": [required_run_rate]
})

prediction = model.predict_proba(live_data)

win_probability = prediction[0][1] * 100
lose_probability = prediction[0][0] * 100

# =========================================
# RAW DATA
# =========================================

st.markdown("---")

st.subheader("📄 Match Data Sample")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.markdown(
    "Built with ❤️ using Streamlit, XGBoost, Machine Learning and Cricket Analytics"
)