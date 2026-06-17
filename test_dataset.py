import pandas as pd

# Load dataset safely
df = pd.read_csv(
    "data/processed/all_matches.csv",
    dtype={"season": str},
    low_memory=False
)

# Basic Preview
print("\n==============================")
print("DATASET PREVIEW")
print("==============================")

print(df.head())

# Dataset Shape
print("\n==============================")
print("SHAPE")
print("==============================")

print(df.shape)

# Columns
print("\n==============================")
print("COLUMNS")
print("==============================")

print(df.columns.tolist())

# Data Types
print("\n==============================")
print("DATA TYPES")
print("==============================")

print(df.dtypes)

# Missing Values
print("\n==============================")
print("MISSING VALUES")
print("==============================")

print(df.isnull().sum())

# Duplicate Rows
print("\n==============================")
print("DUPLICATES")
print("==============================")

print(df.duplicated().sum())

# Dataset Info
print("\n==============================")
print("DATASET INFO")
print("==============================")

print(df.info())