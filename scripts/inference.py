import joblib
import numpy as np

MODEL_PATH = 'models/logistic_sentiment_model.joblib'
VECTORIZER_PATH = 'models/tfidf_vectorizer.joblib'

# 1. Load the files
loaded_model = joblib.load(MODEL_PATH)
loaded_tfidf = joblib.load(VECTORIZER_PATH)

# 2. Test with a new sentence
new_text = "This movie was absolutely terrible and I hated every second!"

# 3. Clean and Vectorize
# Note: Use 'transform' (not fit_transform) so it uses the saved dictionary
def gatekeeper_clean(text):
    text = text.replace('<br />', ' ').replace('<br/>', ' ').replace('<br>', ' ')
    text = ' '.join(text.split())
    return text

def predict_sentiment(new_text):
    clean_text = gatekeeper_clean(new_text)
    vectorized_text = loaded_tfidf.transform([clean_text])
    prediction = loaded_model.predict(vectorized_text)
    score = loaded_model.predict_proba(vectorized_text)
    score = round(np.max(score), 2)
    return prediction[0], int(score * 100)