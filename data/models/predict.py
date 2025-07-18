# ✅ Final predict.py with robust input handling and expected column alignment

import pickle
import pandas as pd
import numpy as np
import os
import json

# Load model, scaler, and expected columns
with open("data/models/mental_health_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("data/models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("data/models/expected_columns.json", "r") as f:
    expected_columns = json.load(f)

# Define suggestions
SUGGESTIONS = {
    0: "Keep journaling, socializing, and exercising to stay balanced.",
    1: "Practice self-care, get enough sleep, and manage work-life balance.",
    2: "Try yoga, breathing exercises, light physical activity.",
    3: "Talk to close ones, reduce screen time, practice meditation.",
    4: "Consider therapy, reach out to professionals, and get social support."
}

# Features that need one-hot encoding
CATEGORICAL_FEATURES = [
    'gender', 'education_level', 'employment_status',
    'medication_use', 'substance_use'
]

# Features that need to be cast to numeric
NUMERIC_FEATURES = [
    'age', 'sleep_hours', 'physical_activity_hrs',
    'social_support_score', 'anxiety_score', 'depression_score', 'stress_level',
    'family_history_mental_illness', 'chronic_illnesses', 'therapy', 'meditation',
    'financial_stress', 'work_stress', 'self_esteem_score', 'life_satisfaction_score',
    'loneliness_score'
]

def predict_mental_state(user_input_dict):
    df = pd.DataFrame([user_input_dict])

    # Strip whitespace and title-case for consistency
    for col in CATEGORICAL_FEATURES:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # Ensure numeric columns are parsed correctly
    for col in NUMERIC_FEATURES:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # One-hot encode categorical features
    df_encoded = pd.get_dummies(df, columns=CATEGORICAL_FEATURES)

    # Reindex to expected columns
    df_encoded = df_encoded.reindex(columns=expected_columns, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df_encoded)

    # Predict
    pred = model.predict(df_scaled)[0]
    suggestion = SUGGESTIONS.get(pred, "No suggestion available.")

    return pred, suggestion
