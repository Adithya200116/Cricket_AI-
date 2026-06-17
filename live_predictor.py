import pandas as pd

from xgboost import XGBClassifier

# Example live situation

live_data = pd.DataFrame([{
    "cumulative_score": 145,
    "wickets_fallen": 4,
    "current_run_rate": 8.2,
    "balls_remaining": 18
}])

# Load training data
X = pd.read_csv("data/processed/X.csv")
y = pd.read_csv("data/processed/y.csv")

y = y.values.ravel()

# Train model
model = XGBClassifier()

model.fit(X, y)

# Predict
probability = model.predict_proba(live_data)

win_probability = probability[0][1] * 100

print(f"Win Probability: {win_probability:.2f}%")