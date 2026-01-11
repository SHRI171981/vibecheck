# VibeCheck: The AI Writing Assistant

**VibeCheck** is a local web application that acts as a "second pair of eyes" for your writing. It analyzes text to determine its emotional tone (Sentiment) and complexity (Readability) using a custom-trained Machine Learning model.

## 🚀 Key Features
* **Custom AI Brain:** Uses a Logistic Regression model (trained on 5,000+ movie reviews) to predict Positive vs. Negative sentiment.
* **Readability Scoring:** Mathematically calculates the grade level required to understand the text (Automated Readability Index).
* **Smart Validation:** "The Gatekeeper" logic filters out spam, profanity, and invalid inputs before processing.
* **Privacy First:** Works 100% offline. No data is sent to external APIs.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Web Framework:** Flask
* **Machine Learning:** Scikit-Learn (TF-IDF + Logistic Regression)
* **Data Processing:** Pandas
* **Frontend:** HTML5, CSS3

## 📂 Project Architecture
The project follows a modular "3-Layer Defense" architecture:
1.  **`rules.py` (The Gatekeeper):** Handles input validation and security checks.
2.  **`train_model.py` (The Gym):** A script to train the AI model and save it as a file.
3.  **`analytics.py` (The Brain):** Loads the saved model to perform inference and calculates stats.
4.  **`app.py` (The Interface):** Connects the backend logic to the web UI.

## Key Variables
1. Input: {"user_id": int, "context": str}
2. Output: {"is_valid": bool, "feedback": str, "sentiment": str, "score": int}

## ⚡ Setup & Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd vibecheck