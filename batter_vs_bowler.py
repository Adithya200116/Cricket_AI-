import pandas as pd

df = pd.read_csv("data/processed/cleaned_matches.csv")

batter = input("Enter Batter: ")
bowler = input("Enter Bowler: ")

matchup = df[
    (df["batter"] == batter) &
    (df["bowler"] == bowler)
]

if len(matchup) == 0:
    print("No data found.")
else:

    runs = matchup["batter_runs"].sum()
    balls = len(matchup)
    wickets = matchup["wicket"].sum()

    strike_rate = (runs / balls) * 100 if balls > 0 else 0

    avg = runs / wickets if wickets > 0 else runs

    print("\nMatchup Analysis")
    print("----------------")
    print("Runs:", runs)
    print("Balls:", balls)
    print("Wickets:", wickets)
    print("Strike Rate:", round(strike_rate, 2))
    print("Average:", round(avg, 2))