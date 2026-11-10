# VibeCheck: AI Writing Assistant

## Problem statement

Short pieces of writing, such as a message, a caption or a review, can come across differently from how you meant them. Writers want a quick second opinion on the tone of what they have written, and the tools that give one usually send your text to an online service.

## Solution

A web app that reads a sentence and tells you whether it sounds positive or negative, with a confidence score. The analysis uses a machine learning model trained on movie reviews and runs entirely on your own machine, so your text never leaves it. A validation layer checks the input first, so only sensible text reaches the model.

## Tech stack

Python, Flask, scikit-learn (TF-IDF and Logistic Regression), Pandas, NumPy, Joblib, HTML and CSS.

## Features

- **Sentiment prediction** (positive or negative) with a confidence score
- **Custom-trained model**: TF-IDF features and Logistic Regression, trained on a labelled movie review dataset
- **Input validation**: text must be between 5 and 50 words and is rejected if it contains abusive language, with a clear message explaining why
- **Cleaning** of leftover HTML line breaks before analysis
- **Runs offline**: no external APIs
- **Clear separation of concerns**: validation rules, training, inference and the web layer are separate modules

## Future steps

- Show a readability score and writing-style suggestions
- Support neutral and mixed sentiment
- Highlight the words that drove the prediction
- Train on a wider set of text types than movie reviews

## Getting started

```bash
pip install -r requirements.txt

# place a labelled dataset (review, sentiment columns) at data/dataset.csv
python scripts/training.py        # trains and saves the model to models/
python app.py
```

Open the local address shown in the terminal and enter a sentence.
