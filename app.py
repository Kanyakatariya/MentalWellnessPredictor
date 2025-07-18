# ✅ Final app.py with complete routing and robust prediction handling

from flask import Flask, render_template, request
import os
from data.models.predict import predict_mental_state

app = Flask(__name__)

# Features required in the form
FEATURES = [
    'age', 'gender', 'education_level', 'employment_status', 'sleep_hours',
    'physical_activity_hrs', 'social_support_score', 'anxiety_score',
    'depression_score', 'stress_level', 'family_history_mental_illness',
    'chronic_illnesses', 'medication_use', 'therapy', 'meditation',
    'substance_use', 'financial_stress', 'work_stress', 'self_esteem_score',
    'life_satisfaction_score', 'loneliness_score'
]

# Define choices for dropdowns (based on training set)
DROPDOWN_OPTIONS = {
    'gender': ['Male', 'Female', 'Other', 'Non-Binary'],
    'education_level': ['High School', "Bachelor's", "Master's", 'PhD', 'Other'],
    'employment_status': ['Employed', 'Unemployed', 'Student', 'Retired'],
    'medication_use': ['Yes', 'No'],
    'substance_use': ['None', 'Occasional', 'Regular'],
    'family_history_mental_illness': ['Yes', 'No'],
    'chronic_illnesses': ['Yes', 'No'],
    'therapy': ['Yes', 'No'],
    'meditation': ['Yes', 'No']
}

# Define color palette for the app (from user-provided theme)
COLOR_PALETTE = {
    'primary': '#222831',  # dark background
    'secondary': '#393E46',  # card color
    'accent': '#948979',     # form input and button
    'highlight': '#DFD0B8',  # text and heading
}

@app.context_processor
def inject_palette():
    return dict(colors=COLOR_PALETTE)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict_form.html', features=FEATURES, dropdowns=DROPDOWN_OPTIONS)

@app.route('/predict-result', methods=['POST'])
def predict_result():
    try:
        user_input = {feature: request.form.get(feature) for feature in FEATURES}
        prediction, suggestion = predict_mental_state(user_input)
        return render_template("predict_result.html", mental_state=prediction, suggestion=suggestion)
    except Exception as e:
        return f"❌ Error during prediction: {str(e)}"

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

if __name__ == '__main__':
    app.run(debug=True)
