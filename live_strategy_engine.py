import pandas as pd
import joblib

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

model = joblib.load(
    "models/cricket_ai_model.pkl"
)

print("=" * 70)
print("LIVE CRICKET STRATEGY ENGINE")
print("=" * 70)

# ==========================================
# BATTER INPUT
# ==========================================

batter_input = input(
    "\nEnter Batter Name: "
)

matches = [

    p for p in df["batter"].dropna().unique()

    if batter_input.lower()
    in str(p).lower()

]

if len(matches) == 0:

    print("No batter found!")

    exit()

print("\nMatching Players:\n")

for i, player in enumerate(matches):

    print(f"{i+1}. {player}")

choice = int(
    input("\nChoose Player Number: ")
)

batter = matches[
    choice - 1
]

print(f"\nSelected Batter: {batter}")

# ==========================================
# MATCH SITUATION
# ==========================================

print("\nCurrent Match Situation")

score = int(
    input("Current Score: ")
)

wickets = int(
    input("Wickets Fallen: ")
)

run_rate = float(
    input("Current Run Rate: ")
)

balls_remaining = int(
    input("Balls Remaining: ")
)

# ==========================================
# WIN PROBABILITY
# ==========================================

live_data = pd.DataFrame([{

    "cumulative_score": score,

    "wickets_fallen": wickets,

    "current_run_rate": run_rate,

    "balls_remaining": balls_remaining

}])

prediction = model.predict_proba(
    live_data
)

win_probability = (
    prediction[0][1] * 100
)

# ==========================================
# BOWLER ANALYSIS
# ==========================================

batter_df = df[
    df["batter"] == batter
]

recommendations = []

for bowler in batter_df[
    "bowler"
].dropna().unique():

    matchup = batter_df[
        batter_df["bowler"] == bowler
    ]

    balls = len(matchup)

    if balls < 10:
        continue

    runs = matchup[
        "batter_runs"
    ].sum()

    dismissals = matchup[
        "wicket"
    ].sum()

    strike_rate = (
        runs / balls
    ) * 100

    average = (
        runs / dismissals
        if dismissals > 0
        else runs
    )

    wicket_probability = (
        dismissals / balls
    ) * 100

    threat_score = (

        wicket_probability * 0.5

        +

        max(
            0,
            200 - strike_rate
        ) * 0.3

        +

        dismissals * 2

    )

    recommendations.append({

        "Bowler":
        bowler,

        "Runs":
        runs,

        "Balls":
        balls,

        "Dismissals":
        dismissals,

        "Average":
        round(
            average,
            2
        ),

        "Strike Rate":
        round(
            strike_rate,
            2
        ),

        "Wicket Probability":
        round(
            wicket_probability,
            2
        ),

        "Threat Score":
        round(
            threat_score,
            2
        )

    })

# ==========================================
# CREATE REPORT
# ==========================================

report = pd.DataFrame(
    recommendations
)

if len(report) == 0:

    print(
        "\nNo matchup data available."
    )

    exit()

report = report.sort_values(

    by="Threat Score",

    ascending=False

)

best = report.iloc[0]

# ==========================================
# RESULTS
# ==========================================

print("\n")
print("=" * 70)
print("LIVE STRATEGY REPORT")
print("=" * 70)

print(
    f"Current Batter : {batter}"
)

print(
    f"Win Probability : {win_probability:.2f}%"
)

print("\n")

print(
    f"Recommended Bowler : {best['Bowler']}"
)

print(
    f"Threat Score : {best['Threat Score']}"
)

print(
    f"Wicket Probability : {best['Wicket Probability']}%"
)

print(
    f"Dismissals : {best['Dismissals']}"
)

print(
    f"Average : {best['Average']}"
)

print(
    f"Strike Rate : {best['Strike Rate']}"
)

# ==========================================
# TOP 5 OPTIONS
# ==========================================

print("\n")
print("=" * 70)
print("TOP 5 BOWLING OPTIONS")
print("=" * 70)

print(

    report[
        [

            "Bowler",

            "Dismissals",

            "Average",

            "Strike Rate",

            "Wicket Probability",

            "Threat Score"

        ]

    ].head(5)

)

# ==========================================
# SAVE REPORT
# ==========================================

report.to_csv(

    "live_strategy_report.csv",

    index=False

)

print(
    "\nStrategy report saved."
)

print(
    "File: live_strategy_report.csv"
)