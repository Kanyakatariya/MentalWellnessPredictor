# 🧠 Mental Health Prediction Web App

This is a full-stack machine learning web application that predicts a user's mental wellness level based on personal and lifestyle inputs. It also offers personalized suggestions such as videos, blogs, and journaling tips to improve mental well-being.

---

## 🌟 Features

- 🧾 Input form with lifestyle and psychological factors
- 🤖 ML-based prediction of mental wellness status: `Well`, `Moderate`, or `Unwell`
- 📊 Trained model with 90–95% accuracy using real-world data
- 🎯 Personalized suggestions page with resources based on prediction
- 💻 User-friendly, modern interface using Bootstrap and Flask

---

## 🛠️ Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| Frontend    | HTML5, CSS3, Bootstrap |
| Backend     | Python, Flask    |
| ML Model    | Scikit-learn, Pandas, NumPy |
| Data        | Kaggle mental health dataset |

---

## 🧠 Input Features

- Age  
- Gender  
- Education Level  
- Employment Status  
- Sleep Hours  
- Physical Activity Hours  
- Social Support Score  
- Anxiety Score  
- Depression Score  
- Life Satisfaction Score  

---

## 📈 Output

A predicted mental wellness state:
- ✅ Well
- ⚠️ Moderate
- ❌ Unwell

The user is redirected to a suggestions page tailored to their result.

---

## 🗂️ Project Structure

MentalWellnessML/
├── app.py
├── requirements.txt
├── templates/
│ ├── index.html
│ ├── prediction.html
│ └── suggestions.html
├── static/
│ └── style.css (optional)
├── data/
│ ├── anxiety_depression_data.csv
│ └── preprocessed_data.csv
├── models/
│ ├── train_model.py
│ ├── predict.py
│ └── suggestion.py
└── README.md

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kanyakatariya/MentalWellnessML.git
   cd MentalWellnessML
Create and activate virtual environment (optional but recommended):
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Access the app:
http://localhost:5000

📚 Resources Used
Scikit-learn
Flask Web Framework
Bootstrap
Kaggle Dataset (Mental Health-related)

👩‍💻 Developer
Mahek Katariya
🎓 Final Year BTech – Computer Engineering
🔗 GitHub | LinkedIn

⚠️ Disclaimer
This app is intended for educational and demonstrative purposes only. It is not a substitute for professional medical advice or diagnosis.

