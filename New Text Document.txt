import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

player = input(
    "Enter Batter Name: "
)

matches = [

    p for p in
    df["batter"].dropna().unique()

    if player.lower()
    in str(p).lower()

]

if len(matches) == 0:

    print("Player not found")
    exit()

print("\nMatching Players:")

for i, p in enumerate(matches):

    print(f"{i+1}. {p}")

choice = int(
    input("Choose Player: ")
)

player = matches[
    choice - 1
]

player_df = df[
    df["batter"] == player
]

innings = (

    player_df.groupby(
        "match_id"
    )["batter_runs"]

    .sum()

    .tail(10)

)

print("\nLast 10 Innings")

print(innings)

form_score = (
    innings.mean()
)

print(
    f"\nForm Score: {form_score:.2f}"
)