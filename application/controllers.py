from flask import Flask, render_template, request, redirect
from scripts.rule import validate_text 
from scripts.inference import predict_sentiment
from application import app

# def validate_text(text):
#     return {"is_valid": True, "feedback": "some feedback"}

# def analyze_context(text):
#     return {"is_valid": True, "feedback": "Good sentence", "sentiment": "Positive", "score": 69}

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/analyze', methods = ['POST'])
def analyze():
    if request.method == 'POST':
        text_input = request.form.get('context')
        user_id = request.form.get('user_id')        
        validation_response = validate_text(text_input)
        if not validation_response['is_valid']:
            return render_template(
                'feedback.html',
                is_valid = False,
                original_text = text_input,
                feedback = validation_response['feedback']
            )

        prediction, score = predict_sentiment(text_input)
        return render_template(
            'feedback.html',
            is_valid = True,
            original_text = text_input,
            sentiment = prediction.capitalize(),
            score = score,
            feedback = "Good sentence"
        )