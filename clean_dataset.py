import pandas as pd

df = pd.read_csv("data/processed/all_matches.csv")

# Fill missing values
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("data/processed/cleaned_matches.csv", index=False)

print("Dataset cleaned successfully!")
print(df.shape)