import requests
import pandas as pd
import os

# always save relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

API_KEY = "d5d1121a821c4663b41c9960b1bdc2af"

query = "TCS OR Infosys OR Reliance"
url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={API_KEY}"

response = requests.get(url).json()

articles = []
for a in response.get("articles", []):
    articles.append({
        "title": a["title"],
        "description": a["description"],
        "source": a["source"]["name"],
        "publishedAt": a["publishedAt"]
    })

df = pd.DataFrame(articles)
file_path = os.path.join(DATA_DIR, "news.csv")
df.to_csv(file_path, index=False)

print(f"News saved to {file_path}")
