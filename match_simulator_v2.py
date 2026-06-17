import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/cleaned_matches.csv",
    low_memory=False
)

score = int(input("Current Score: "))
wickets = int(input("Wickets Fallen: "))
balls_remaining = int(input("Balls Remaining: "))

simulations = 5000

scores = []

for _ in range(simulations):

    current = score

    wickets_left = 10 - wickets

    for ball in range(balls_remaining):

        run = np.random.choice(
            [0,1,2,3,4,6],
            p=[0.30,0.35,0.10,0.03,0.17,0.05]
        )

        current += run

        wicket = np.random.choice(
            [0,1],
            p=[0.97,0.03]
        )

        if wicket:

            wickets_left -= 1

            if wickets_left <= 0:
                break

    scores.append(current)

print("\nMATCH SIMULATION REPORT")
print("-" * 50)

print(
    "Projected Score:",
    round(np.mean(scores))
)

print(
    "Best Case:",
    max(scores)
)

print(
    "Worst Case:",
    min(scores)
)

print(
    "Median:",
    round(np.median(scores))
)