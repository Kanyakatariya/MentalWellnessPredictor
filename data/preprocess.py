import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/anxiety_depression_data.csv")

# Standardize column names
df.columns = [col.lower() for col in df.columns]

# Handle missing values (numerical only)
df = df.fillna(df.mean(numeric_only=True))

# Scoring-based label for mental state
def classify_mental_state(row):
    score = 0
    score += row.get('stress_level', 0)
    score += row.get('anxiety_score', 0)
    score += row.get('depression_score', 0)
    score -= row.get('self_esteem_score', 0)
    score += row.get('loneliness_score', 0)
    score -= row.get('life_satisfaction_score', 0)

    if score < 3:
        return 0  # Mentally Well
    elif score < 6:
        return 1  # Moderate
    elif score < 9:
        return 2  # Stressed
    elif score < 12:
        return 3  # Unwell
    else:
        return 4  # Critical

# Apply function to create label
df["mental_state"] = df.apply(classify_mental_state, axis=1)

# Print confirmation
print("✅ Sample of mental_state column values:\n", df["mental_state"].value_counts())

# Save to CSV
os.makedirs("data", exist_ok=True)
df.to_csv("preprocessed_data.csv", index=False)
print("✅ Saved 'preprocessed_data.csv' with 'mental_state' column.")
