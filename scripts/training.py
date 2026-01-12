import pandas as pd
import re
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

df=pd.read_csv(r"data/dataset.csv")

def gatekeeper_clean(text):
    text = text.replace('<br />', ' ').replace('<br/>', ' ').replace('<br>', ' ')
    text = ' '.join(text.split())
    return text

df['review'] = df['review'].apply(gatekeeper_clean)

X = df['review'] 
y = df['sentiment']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tfidf = TfidfVectorizer(max_features=5000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train_tfidf, y_train)

y_pred = lr_model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print(f"Logistic Regression Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Performance Report:")
print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))

joblib.dump(lr_model, 'models/logistic_sentiment_model.joblib')
joblib.dump(tfidf, 'models/tfidf_vectorizer.joblib')