import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

if "winner" not in df.columns:
    print("winner column missing")
    exit()

venue = input("Enter Venue: ")

venue_df = df[
    df["venue"]
    .astype(str)
    .str.contains(
        venue,
        case=False,
        na=False
    )
]

if len(venue_df) == 0:
    print("Venue not found")
    exit()

wins = (

    venue_df.groupby(
        "winner"
    )["match_id"]

    .nunique()

    .sort_values(
        ascending=False
    )

)

print("\nVENUE WIN REPORT")
print("-" * 50)

print(wins.head(10))