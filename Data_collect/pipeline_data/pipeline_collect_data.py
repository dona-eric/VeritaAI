import requests, psycopg2, schedule, time
import os, pathlib, dotenv
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY_NEWS = os.getenv("API_KEY_NEWS")
# Requêtes ciblées sur les sujets
CATEGORY = [
    "politics",
    "education",
    "cybercriminality",
    "technology",
    "health",
    "entertainment",
    "sports",
    "business",
    "climate change",
    "artificial intelligence",
    "cryptocurrency",
    "blockchain",
    "data privacy",
    "social media",
    "bitcoin"
    
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

def fetch_and_store():
    connection_database = psycopg2.connect(**DB_PARAMS)
    cursor_connect = connection_database.cursor()
    for category in CATEGORY:
        url = f"https://newsapi.org/v2/top-headlines?q={category}&language=en&from={today}&pageSize=100&apiKey={API_KEY_NEWS}"
        response = requests.get(url)
        articles = response.json().get("articles", [])

        for article in articles:
            cursor_connect.execute("""
                INSERT INTO news (title, description, author, content, published_at, source, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING 
                    """, (
                        article.get("title"),
                        article.get("description"),
                        article.get("author"),
                        article.get("content"),
                        article.get("publishedAt"),
                        article["source"]["name"],
                        category  # Utiliser la requête comme catégorie
                    ))
    
    connection_database.commit()
    cursor_connect.close()
    connection_database.close()
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
