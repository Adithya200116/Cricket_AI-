import pandas as pd
import joblib

print("=" * 60)
print("CRICKET AI WIN PROBABILITY ENGINE")
print("=" * 60)

model = joblib.load(
    "models/cricket_ai_model.pkl"
)

score = int(input("Current Score: "))
wickets = int(input("Wickets Fallen: "))
run_rate = float(input("Current Run Rate: "))
balls_remaining = int(input("Balls Remaining: "))

live_data = pd.DataFrame([{
    "cumulative_score": score,
    "wickets_fallen": wickets,
    "current_run_rate": run_rate,
    "balls_remaining": balls_remaining
}])

prediction = model.predict_proba(
    live_data
)

win_probability = (
    prediction[0][1] * 100
)

print("\n")
print("=" * 60)
print("RESULT")
print("=" * 60)

print(
    f"Win Probability: {win_probability:.2f}%"
)