import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

player = input("Enter Batter Name: ")
team = input("Enter Bowling Team: ")

player_df = df[
    df["batter"].str.contains(
        player,
        case=False,
        na=False
    )
]

if "bowling_team" not in df.columns:
    print("bowling_team column not found!")
    exit()

matchup = player_df[
    player_df["bowling_team"]
    .str.contains(
        team,
        case=False,
        na=False
    )
]

if len(matchup) == 0:
    print("No data found.")
    exit()

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

print("\nPLAYER VS TEAM REPORT")
print("-" * 50)

print("Runs:", runs)
print("Balls:", balls)
print("Dismissals:", dismissals)
print("Average:", round(average,2))
print("Strike Rate:", round(strike_rate,2))