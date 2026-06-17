import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

print("=" * 70)
print("CRICKET AI CAPTAIN ENGINE")
print("=" * 70)

# ==========================================
# FIND BATTER
# ==========================================

batter_input = input(
    "\nEnter Batter Name: "
)

matches = [
    p for p in df["batter"].dropna().unique()
    if batter_input.lower() in str(p).lower()
]

if len(matches) == 0:

    print("No batter found!")
    exit()

print("\nMatching Players:")

for i, player in enumerate(matches):

    print(f"{i+1}. {player}")

choice = int(
    input("\nChoose Player Number: ")
)

batter = matches[choice - 1]

# ==========================================
# FILTER BATTER DATA
# ==========================================

batter_df = df[
    df["batter"] == batter
]

recommendations = []

for bowler in batter_df["bowler"].dropna().unique():

    matchup = batter_df[
        batter_df["bowler"] == bowler
    ]

    runs = matchup["batter_runs"].sum()

    balls = len(matchup)

    dismissals = matchup["wicket"].sum()

    strike_rate = (
        runs / balls * 100
        if balls > 0 else 0
    )

    average = (
        runs / dismissals
        if dismissals > 0 else runs
    )

    threat_score = (
        dismissals * 25
    ) + (
        max(0, 200 - strike_rate)
        * 0.2
    )

    recommendations.append({

        "Bowler": bowler,
        "Dismissals": dismissals,
        "Runs": runs,
        "Balls": balls,
        "Average": round(average, 2),
        "Strike Rate": round(strike_rate, 2),
        "Threat Score": round(threat_score, 2)

    })

report = pd.DataFrame(
    recommendations
)

report = report.sort_values(
    by="Threat Score",
    ascending=False
)

best = report.iloc[0]

print("\n")
print("=" * 70)
print("CAPTAIN RECOMMENDATION")
print("=" * 70)

print(
    f"Recommended Bowler: {best['Bowler']}"
)

print(
    f"Threat Score: {best['Threat Score']}"
)

print(
    f"Dismissals: {best['Dismissals']}"
)

print(
    f"Average: {best['Average']}"
)

print(
    f"Strike Rate: {best['Strike Rate']}"
)

report.to_csv(
    "captain_recommendation_report.csv",
    index=False
)

print(
    "\nReport Saved Successfully!"
)