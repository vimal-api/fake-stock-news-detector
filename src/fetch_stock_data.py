import yfinance as yf
import pandas as pd

stocks = ["TCS.NS", "INFY.NS", "RELIANCE.NS"]

all_data = []

for stock in stocks:
    print(f"Fetching data for {stock}")
    df = yf.download(stock, period="30d", interval="1d")
    df["Stock"] = stock
    all_data.append(df)

final = pd.concat(all_data)
final.reset_index(inplace=True)

final.to_csv("data/stock_prices.csv", index=False)

print("Stock data saved to data/stock_prices.csv")
