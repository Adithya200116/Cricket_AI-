import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

print("=" * 60)
print("MATCH SIMULATOR")
print("=" * 60)

score = int(input("Current Score: "))
wickets = int(input("Wickets Fallen: "))
balls_remaining = int(input("Balls Remaining: "))

avg_runs_per_ball = (
    df["total_runs"].mean()
)

simulations = 1000

results = []

for _ in range(simulations):

    current = score

    wickets_left = 10 - wickets

    for ball in range(balls_remaining):

        run = np.random.choice(
            [0,1,2,3,4,6],
            p=[0.35,0.35,0.10,0.02,0.15,0.03]
        )

        current += run

        if np.random.random() < 0.03:

            wickets_left -= 1

            if wickets_left <= 0:
                break

    results.append(current)

print("\nProjected Score:",
      round(np.mean(results)))

print("Best Case:",
      max(results))

print("Worst Case:",
      min(results))