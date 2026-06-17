import pandas as pd

df = pd.read_csv("data/processed/cleaned_matches.csv")

# Create target column
df["result"] = (
    df["batting_team"] == df["winner"]
).astype(int)

# Features
features = [
    "cumulative_score",
    "wickets_fallen",
    "current_run_rate",
    "balls_remaining"
]

X = df[features]

y = df["result"]

print(X.head())
print(y.head())

# Save
X.to_csv("data/processed/X.csv", index=False)
y.to_csv("data/processed/y.csv", index=False)

print("Training data prepared!")