import pandas as pd

# Load your dataset
df = pd.read_csv("data/anxiety_depression_data.csv")

# Explore basic structure
print("🧠 Shape of dataset:", df.shape)
print("\n📌 Column names:", df.columns.tolist())
print("\n🔍 Missing values:\n", df.isnull().sum())
print("\n🔎 Data preview:\n", df.head())
