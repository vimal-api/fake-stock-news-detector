
# Fake Stock News & Market Manipulation Detector
This project was built to understand how fake or exaggerated stock-related news can influence market prices and create misleading trends for retail investors.
The system uses real stock data and real financial news, applies sentiment analysis, and checks whether unusual price movements happened after high-emotion news.

What this project does

The system follows these steps:
1. Fetches stock prices for selected Indian companies (TCS, Infosys, Reliance)  
2. Collects financial news headlines related to these companies  
3. Performs sentiment analysis on the news  
4. Detects suspicious price movements based on news sentiment  
5. Visualizes risky days using a graph

Why this matters

In real markets, fake or misleading news is often used to create hype or panic, which can lead to wrong investment decisions.  
This project shows how data and AI can be used to detect such behaviour using actual market data.

Tech Stack

- Python  
- yfinance  
- News API  
- Pandas  
- TextBlob  
- Matplotlib  

Project Structure

fake-stock-news-detector/
├── src/
│ ├── fetch_stock_data.py
│ ├── fetch_news.py
│ ├── sentiment.py
│ ├── market_anomaly.py
│ └── plot.py
│
├── data/
│ ├── stock_prices.csv
│ ├── news.csv
│ ├── news_with_sentiment.csv
│ └── market_risk.csv
│
└── README.md

How to run

1. Install required libraries  
pip install yfinance pandas textblob matplotlib requests

2. Fetch stock prices  
python src/fetch_stock_data.py

3. Fetch news  
python src/fetch_news.py

4. Run sentiment analysis  
python src/sentiment.py

5. Detect market manipulation  
python src/market_anomaly.py

7. View the visualization  
python src/plot.py

Output
   
The system creates:
- market_risk.csv which shows stock price, sentiment, and suspicious flags  
- a graph that highlights possible manipulation days  

Red points on the graph represent high-risk days where price and news sentiment move together.

Learning Outcome

This project helped me understand:
- how stock data is collected  
- how news sentiment affects markets  
- how data analytics can be used to detect financial risk  

It combines finance, data analysis, and AI into one practical project.




