import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

stock_path = os.path.join(DATA_DIR, "stock_prices.csv")
news_path = os.path.join(DATA_DIR, "news_with_sentiment.csv")

stocks = pd.read_csv(stock_path)
news = pd.read_csv(news_path)

# Convert to correct types
stocks["Date"] = pd.to_datetime(stocks["Date"])
stocks["Close"] = pd.to_numeric(stocks["Close"], errors="coerce")

news["publishedAt"] = pd.to_datetime(news["publishedAt"])
news["sentiment"] = pd.to_numeric(news["sentiment"], errors="coerce")

# Daily aggregates
daily_price = stocks.groupby(stocks["Date"].dt.date)["Close"].mean()
daily_sentiment = news.groupby(news["publishedAt"].dt.date)["sentiment"].mean()

combined = pd.concat([daily_price, daily_sentiment], axis=1)
combined.columns = ["avg_price", "sentiment"]
combined = combined.dropna()

# % price change
combined["price_change"] = combined["avg_price"].pct_change()

# Flag suspicious days
combined["suspicious"] = (combined["price_change"].abs() > 0.03) & (combined["sentiment"].abs() > 0.2)

out_path = os.path.join(DATA_DIR, "market_risk.csv")
combined.to_csv(out_path)

print(f"Market risk analysis saved → {out_path}")
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

stock_path = os.path.join(DATA_DIR, "stock_prices.csv")
news_path = os.path.join(DATA_DIR, "news_with_sentiment.csv")

stocks = pd.read_csv(stock_path)
news = pd.read_csv(news_path)

# Convert to correct types
stocks["Date"] = pd.to_datetime(stocks["Date"])
stocks["Close"] = pd.to_numeric(stocks["Close"], errors="coerce")

news["publishedAt"] = pd.to_datetime(news["publishedAt"])
news["sentiment"] = pd.to_numeric(news["sentiment"], errors="coerce")

# Daily aggregates
daily_price = stocks.groupby(stocks["Date"].dt.date)["Close"].mean()
daily_sentiment = news.groupby(news["publishedAt"].dt.date)["sentiment"].mean()

combined = pd.concat([daily_price, daily_sentiment], axis=1)
combined.columns = ["avg_price", "sentiment"]
combined = combined.dropna()

# % price change
combined["price_change"] = combined["avg_price"].pct_change()

# Flag suspicious days
combined["suspicious"] = (combined["price_change"].abs() > 0.03) & (combined["sentiment"].abs() > 0.2)

out_path = os.path.join(DATA_DIR, "market_risk.csv")
combined.to_csv(out_path)

print(f"Market risk analysis saved → {out_path}")
