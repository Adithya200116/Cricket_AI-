import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

print("=" * 70)
print("CRICKET AI - BOWLER RECOMMENDATION ENGINE")
print("=" * 70)

# ==========================================
# FIND BATTER
# ==========================================

batter_input = input(
    "\nEnter Batter Name (Example: kohli): "
)

matches = [
    p for p in df["batter"].dropna().unique()
    if batter_input.lower() in str(p).lower()
]

if len(matches) == 0:

    print("\nNo player found!")

    exit()

print("\nMatching Players:")

for i, player in enumerate(matches):

    print(f"{i+1}. {player}")

choice = int(
    input("\nChoose Player Number: ")
)

batter = matches[choice - 1]

print(f"\nSelected Batter: {batter}")

# ==========================================
# FILTER DATA
# ==========================================

batter_df = df[
    df["batter"] == batter
]

# ==========================================
# ANALYZE BOWLERS
# ==========================================

recommendations = []

for bowler in batter_df["bowler"].dropna().unique():

    matchup = batter_df[
        batter_df["bowler"] == bowler
    ]

    runs = matchup["batter_runs"].sum()

    balls = len(matchup)

    dismissals = matchup["wicket"].sum()

    strike_rate = (
        (runs / balls) * 100
        if balls > 0
        else 0
    )

    average = (
        runs / dismissals
        if dismissals > 0
        else runs
    )

    total_runs = matchup["total_runs"].sum()

    overs = balls / 6

    economy = (
        total_runs / overs
        if overs > 0
        else 0
    )

    # Lower score = better bowler

    score = (
        average * 0.5
        +
        strike_rate * 0.3
        +
        economy * 0.2
    )

    recommendations.append({

        "Bowler": bowler,
        "Runs": runs,
        "Balls": balls,
        "Dismissals": dismissals,
        "Average": round(average, 2),
        "Strike Rate": round(strike_rate, 2),
        "Economy": round(economy, 2),
        "Recommendation Score": round(score, 2)

    })

# ==========================================
# CREATE REPORT
# ==========================================

report = pd.DataFrame(
    recommendations
)

report = report.sort_values(
    by=[
        "Dismissals",
        "Recommendation Score"
    ],
    ascending=[
        False,
        True
    ]
)

# ==========================================
# TOP RECOMMENDATIONS
# ==========================================

print("\n")
print("=" * 70)
print("TOP 10 BOWLER RECOMMENDATIONS")
print("=" * 70)

print(
    report.head(10).to_string(index=False)
)

# ==========================================
# BEST BOWLER
# ==========================================

best = report.iloc[0]

print("\n")
print("=" * 70)
print("BEST BOWLER AGAINST THIS BATTER")
print("=" * 70)

print(f"Bowler      : {best['Bowler']}")
print(f"Dismissals  : {best['Dismissals']}")
print(f"Runs Given  : {best['Runs']}")
print(f"Balls Bowled: {best['Balls']}")
print(f"Average     : {best['Average']}")
print(f"Strike Rate : {best['Strike Rate']}")
print(f"Economy     : {best['Economy']}")

# ==========================================
# WEAKNESS SUMMARY
# ==========================================

print("\n")
print("=" * 70)
print("BATTER WEAKNESS SUMMARY")
print("=" * 70)

for i in range(
    min(5, len(report))
):

    row = report.iloc[i]

    print(
        f"{i+1}. {row['Bowler']} "
        f"| Dismissals: {row['Dismissals']} "
        f"| Average: {row['Average']} "
        f"| SR: {row['Strike Rate']}"
    )

# ==========================================
# SAVE REPORT
# ==========================================

filename = (
    batter.replace(" ", "_")
    + "_bowler_report.csv"
)

report.to_csv(
    filename,
    index=False
)

print("\n")
print("=" * 70)
print("REPORT SAVED SUCCESSFULLY")
print("=" * 70)

print(f"File Name: {filename}")

print("\nAnalysis Complete.")