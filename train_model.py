import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

print("=" * 50)
print("CRICKET AI MODEL TRAINING")
print("=" * 50)

# =========================================
# LOAD DATA
# =========================================

dataset_path = "data/processed/cleaned_matches.csv"

if not os.path.exists(dataset_path):
    print(f"ERROR: Dataset not found -> {dataset_path}")
    exit()

df = pd.read_csv(dataset_path)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# =========================================
# CREATE TARGET
# =========================================

df["result"] = (
    df["batting_team"] == df["winner"]
).astype(int)

# =========================================
# FEATURES
# =========================================

features = [

    "innings",

    "over",

    "cumulative_score",

    "wickets_fallen",

    "current_run_rate",

    "target_runs",

    "balls_remaining",

    "required_run_rate"

]

X = df[features]
y = df["result"]

print("\nFeatures Selected:")
print(features)

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Started...")

# =========================================
# MODEL
# =========================================

model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)

# =========================================
# TRAIN
# =========================================

model.fit(X_train, y_train)

print("Training Completed!")

# =========================================
# EVALUATE
# =========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# =========================================
# CREATE MODELS DIRECTORY
# =========================================

models_folder = "models"

os.makedirs(
    models_folder,
    exist_ok=True
)

print(f"\nModels folder verified: {models_folder}")

# =========================================
# SAVE MODEL
# =========================================

model_path = os.path.join(
    models_folder,
    "cricket_ai_model.pkl"
)

joblib.dump(
    model,
    model_path
)

print(f"\nModel saved successfully!")
print(f"Path: {os.path.abspath(model_path)}")

# =========================================
# VERIFY FILE EXISTS
# =========================================

if os.path.exists(model_path):

    print("\nModel file verified!")
    print("READY FOR DASHBOARD")

else:

    print("\nERROR: Model file not found after saving!")

# =========================================
# END
# =========================================

print("\nEND OF SCRIPT REACHED")
print("=" * 50)