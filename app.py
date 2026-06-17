import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cricket Strategy AI",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/cleaned_matches.csv",
        low_memory=False
    )

df = load_data()

st.title("🏏 Cricket Strategy AI")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Home"]
)

if menu == "Home":

    st.header("Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Matches",
        df["match_id"].nunique()
    )

    c2.metric(
        "Deliveries",
        len(df)
    )

    c3.metric(
        "Batters",
        df["batter"].nunique()
    )

    c4.metric(
        "Bowlers",
        df["bowler"].nunique()
    )