import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Cricket AI",
    layout="wide"
)

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

model = joblib.load(
    "models/cricket_ai_model.pkl"
)

st.title(
    "🏏 Cricket Strategy AI"
)

tab1, tab2, tab3 = st.tabs(
    [
        "Analytics",
        "Win Predictor",
        "Player Analysis"
    ]
)

# ====================================
# TAB 1
# ====================================

with tab1:

    st.subheader(
        "Top Run Scorers"
    )

    top_batters = (

        df.groupby(
            "batter"
        )["batter_runs"]

        .sum()

        .sort_values(
            ascending=False
        )

        .head(10)

        .reset_index()

    )

    fig = px.bar(
        top_batters,
        x="batter",
        y="batter_runs"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ====================================
# TAB 2
# ====================================

with tab2:

    score = st.number_input(
        "Score",
        0,
        300,
        150
    )

    wickets = st.number_input(
        "Wickets",
        0,
        10,
        3
    )

    run_rate = st.number_input(
        "Run Rate",
        0.0,
        20.0,
        8.5
    )

    balls = st.number_input(
        "Balls Remaining",
        0,
        120,
        24
    )

    live = pd.DataFrame([{

        "cumulative_score":
        score,

        "wickets_fallen":
        wickets,

        "current_run_rate":
        run_rate,

        "balls_remaining":
        balls

    }])

    prediction = (
        model.predict_proba(
            live
        )[0][1]
    ) * 100

    st.metric(
        "Win Probability",
        f"{prediction:.2f}%"
    )

# ====================================
# TAB 3
# ====================================

with tab3:

    player = st.text_input(
        "Player Name"
    )

    if player:

        filtered = df[

            df["batter"]

            .str.contains(
                player,
                case=False,
                na=False
            )

        ]

        runs = filtered[
            "batter_runs"
        ].sum()

        st.metric(
            "Career Runs",
            runs
        )