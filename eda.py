import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_matches.csv")

# Top run scorers
top_batters = (
    df.groupby("batter")["batter_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_batters)

# Plot
top_batters.plot(kind="bar")

plt.title("Top Run Scorers")
plt.xlabel("Batter")
plt.ylabel("Runs")

plt.show()