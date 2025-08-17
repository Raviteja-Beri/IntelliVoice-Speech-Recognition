# intellivoice/modules/intent_detector.py
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Intent samples for training
samples = [
    ("play some music", "play_song"),
    ("play despacito", "play_song"),
    ("what's the weather like", "get_weather"),
    ("tell me the news", "get_news"),
    ("make me laugh", "joke"),
    ("tell me a joke", "joke"),
    ("who are you", "identity"),
    ("what can you do", "identity"),
    ("what time is it", "get_time")
]

X = [x[0] for x in samples]
y = [x[1] for x in samples]

# Train or load model
model_path = "intellivoice/data/intent_model.pkl"
os.makedirs(os.path.dirname(model_path), exist_ok=True)

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    model.fit(X, y)
    joblib.dump(model, model_path)

def get_intent(text):
    if not text.strip():
        return ("", 0.0)
    probs = model.predict_proba([text])[0]
    idx = probs.argmax()
    return (model.classes_[idx], probs[idx])
