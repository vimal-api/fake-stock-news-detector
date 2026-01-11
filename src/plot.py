import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

data = pd.read_csv(os.path.join(DATA_DIR, "market_risk.csv"))

plt.figure(figsize=(10,5))
plt.plot(data["avg_price"], label="Stock Price")
plt.plot(data["sentiment"] * data["avg_price"].mean(), label="News Sentiment (scaled)")

for i in range(len(data)):
    if data["suspicious"][i] == True:
        plt.scatter(i, data["avg_price"][i])

plt.title("Stock Price vs News Sentiment (Suspicious Days Highlighted)")
plt.legend()
plt.show()


