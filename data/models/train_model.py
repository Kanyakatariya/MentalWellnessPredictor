# ✅ Updated train_model.py with improved accuracy using SMOTE and XGBoost

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
import pickle
import os
import json

# Load data
df = pd.read_csv("../data/preprocessed_data.csv")
df.columns = [col.lower() for col in df.columns]  # standardize column names
print("🧪 Columns after lowercasing:", df.columns.tolist())

# Check for mental_state column
if 'mental_state' not in df.columns:
    raise ValueError("❌ 'mental_state' column not found in preprocessed_data.csv")

# Encode categorical columns
categorical_cols = ["gender", "education_level", "employment_status", "medication_use", "substance_use"]
print("🔠 Encoding columns:", categorical_cols)
df = pd.get_dummies(df, columns=categorical_cols)

# Features and target
X = df.drop("mental_state", axis=1)
y = df["mental_state"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Handle class imbalance
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1, eval_metric='mlogloss', random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Cross-validation accuracy
cv_scores = cross_val_score(model, X_resampled, y_resampled, cv=5)
print("\n📈 Cross-validation Accuracy:", cv_scores.mean())

# Save model
os.makedirs("models", exist_ok=True)
with open("../models/mental_health_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("\n✅ Model saved at: models/mental_health_model.pkl")

# Save scaler
with open("../models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save expected columns
with open("../models/expected_columns.json", "w") as f:
    json.dump(list(X.columns), f)

# Sample prediction
sample_input = X.iloc[0:1]
sample_input_scaled = scaler.transform(sample_input)
pred = model.predict(sample_input_scaled)[0]

mental_states = {
    0: "Mentally Well",
    1: "Moderate",
    2: "Stressed",
    3: "Unwell",
    4: "Critical"
}

suggestions = {
    0: "Keep journaling, socializing, and exercising to stay balanced.",
    1: "Practice self-care, get enough sleep, and manage work-life balance.",
    2: "Try yoga, breathing exercises, light physical activity.",
    3: "Talk to close ones, reduce screen time, practice meditation.",
    4: "Consider therapy, reach out to professionals, and get social support."
}

print("\n🧠 Predicted mental state:", pred)
print("💡 Suggestion:", suggestions.get(pred, "No suggestion available."))
