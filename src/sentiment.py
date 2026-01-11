import pandas as pd
import os
from textblob import TextBlob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

news_path = os.path.join(DATA_DIR, "news.csv")
news = pd.read_csv(news_path)

def get_sentiment(text):
    if pd.isna(text):
        return 0
    return TextBlob(text).sentiment.polarity

news["sentiment"] = news["title"].apply(get_sentiment)

out_path = os.path.join(DATA_DIR, "news_with_sentiment.csv")
news.to_csv(out_path, index=False)

print(f"Sentiment added → {out_path}")
