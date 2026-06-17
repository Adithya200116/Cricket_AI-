import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

print("=" * 60)
print("WICKET PROBABILITY ENGINE")
print("=" * 60)

batter = input(
    "\nEnter Batter Name: "
)

bowler = input(
    "Enter Bowler Name: "
)

matchup = df[
    (df["batter"].str.contains(
        batter,
        case=False,
        na=False
    ))
    &
    (df["bowler"].str.contains(
        bowler,
        case=False,
        na=False
    ))
]

if len(matchup) == 0:

    print(
        "\nNo matchup data found."
    )

    exit()

balls = len(matchup)

dismissals = matchup[
    "wicket"
].sum()

wicket_probability = (
    dismissals / balls
) * 100

runs = matchup[
    "batter_runs"
].sum()

strike_rate = (
    runs / balls
) * 100

print("\n")
print("=" * 60)
print("MATCHUP ANALYSIS")
print("=" * 60)

print("Balls:", balls)

print("Dismissals:", dismissals)

print(
    f"Wicket Probability: {wicket_probability:.2f}%"
)

print(
    f"Strike Rate: {strike_rate:.2f}"
)