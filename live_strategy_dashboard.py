import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Cricket Strategy AI",
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
    "🏏 Cricket Strategy AI Platform"
)

tab1, tab2, tab3 = st.tabs(
    [
        "Win Predictor",
        "Match Simulator",
        "Team Strength"
    ]
)

# =====================================
# TAB 1
# =====================================

with tab1:

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

    rr = st.number_input(
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
        rr,

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

# =====================================
# TAB 2
# =====================================

with tab2:

    sim_score = st.number_input(
        "Current Score",
        0,
        300,
        160
    )

    sim_wickets = st.number_input(
        "Wickets Fallen",
        0,
        10,
        4
    )

    sim_balls = st.number_input(
        "Balls Left",
        0,
        120,
        18
    )

    if st.button(
        "Run Simulation"
    ):

        results = []

        for _ in range(1000):

            total = sim_score

            wickets_left = (
                10 - sim_wickets
            )

            for ball in range(
                sim_balls
            ):

                total += np.random.choice(
                    [0,1,2,3,4,6]
                )

                if np.random.random() < 0.03:

                    wickets_left -= 1

                    if wickets_left <= 0:
                        break

            results.append(total)

        st.metric(
            "Projected Score",
            round(
                np.mean(results)
            )
        )

# =====================================
# TAB 3
# =====================================

with tab3:

    team = st.text_input(
        "Team Name"
    )

    if team:

        team_df = df[
            df["batting_team"]
            .str.contains(
                team,
                case=False,
                na=False
            )
        ]

        if len(team_df):

            batting = (
                team_df[
                    "batter_runs"
                ].mean()
            )

            bowling = (
                team_df[
                    "wicket"
                ].mean()
                * 100
            )

            st.metric(
                "Batting Strength",
                round(
                    batting,
                    2
                )
            )

            st.metric(
                "Bowling Strength",
                round(
                    bowling,
                    2
                )
            )