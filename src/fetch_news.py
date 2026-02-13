import feedparser
import pandas as pd
from datetime import datetime

RSS_URL = "https://www.moneycontrol.com/rss/marketreports.xml"

def fetch_news():
    feed = feedparser.parse(RSS_URL)
    rows = []

    for entry in feed.entries:
        rows.append({
            "timestamp": datetime.now(),
            "source": "Moneycontrol",
            "text": entry.title
        })

    df = pd.DataFrame(rows)
    df.to_csv("../data/raw_news.csv", mode="a", header=False, index=False)
    print("News data appended successfully.")

if __name__ == "__main__":
    fetch_news()