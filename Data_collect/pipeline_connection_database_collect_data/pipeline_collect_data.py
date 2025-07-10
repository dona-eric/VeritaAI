import requests, psycopg2, schedule, time
import os, pathlib, dotenv
from datetime import date, datetime
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, String, Text
from model import News, Base
from sqlalchemy.orm import sessionmaker
load_dotenv()

API_KEY_NEWS = os.getenv("API_KEY_NEWS")
# Requêtes ciblées sur les sujets
CATEGORY = ["politics","education","cybercriminality","technology",
    "health","entertainment","sports","business","climate change",
    "artificial intelligence","cryptocurrency","blockchain","data privacy",
    "social media","bitcoin"
]

# date of the last update
today = date.today().isoformat()
DB_PARAMS = {
    "host": os.getenv("host"),
    "dbname": os.getenv("dbname"),
    "user": os.getenv("user"),
    "password": os.getenv("password"),
    "port": os.getenv("port")
}

# session engine
engine = create_engine(f"postgresql://{DB_PARAMS['user']}:{DB_PARAMS['password']}@{DB_PARAMS['host']}:{DB_PARAMS['port']}/{DB_PARAMS['dbname']}")

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def fetch_and_store():
    session = Session()
    for category in CATEGORY:
        url = f"https://newsapi.org/v2/top-headlines?q={category}&language=en&from={today}&pageSize=100&apiKey={API_KEY_NEWS}"
        response = requests.get(url)
        articles = response.json().get("articles", [])

        for article in articles:
            if article.get("title"):
                        news_item = News(
                            title=article.get("title"),
                            description=article.get("description"),
                            author=article.get("author"),
                            content=article.get("content"),
                            published_at=datetime.strptime(article.get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ"),
                            source=article["source"]["name"],
                            category=category  # Utiliser la requête comme catégorie
                        )
                        session.merge(news_item)
    
    
    session.commit()
    session.close()
    print(f"[{datetime.now()}] ✅ Données mises à jour.")

# Planifier l’exécution toutes les 1 minutes
schedule.every(1).minutes.do(fetch_and_store)

# Boucle principale
if __name__ == "__main__":
    print("🚀 Démarrage du collecteur NewsAPI (intervalle : 1 min)...")
    fetch_and_store()  # exécution initiale
    while True:
        schedule.run_pending()
        time.sleep(1)
