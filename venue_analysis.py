import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

print("=" * 60)
print("VENUE ANALYSIS")
print("=" * 60)

venue_stats = (

    df.groupby(
        "venue"
    )["total_runs"]

    .mean()

    .sort_values(
        ascending=False
    )

)

print(
    venue_stats.head(15)
)

best = venue_stats.index[0]

print("\nBest Batting Venue:")

print(best)

print(
    f"Average Runs: {venue_stats.iloc[0]:.2f}"
)