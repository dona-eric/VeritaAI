import os, requests, dotenv, psycopg2, schedule, logging, time
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv

# charger les variables d'environnement depuis le fichier .env
load_dotenv()

# settings of database
DB_PARAMS = {
    "host": os.getenv("host"),
    "dbname": os.getenv("dbname"),
    "user": os.getenv("user"),
    "password": os.getenv("password"),
    "port": os.getenv("port")
}
file = "True_news"
def automatise_data_save():
    try:
        connection_data = psycopg2.connect(**DB_PARAMS)
        cursor_server = connection_data.cursor()

        cursor_server.execute("SELECT title, description, author, content, published_at, source, category FROM news;")
        data_rows = cursor_server.fetchall()

        data_columns = [col[0] for col in cursor_server.description]

        df = pd.DataFrame(data_rows, columns=data_columns)

        # save to csv
        df.to_csv(file, index=False)

        logging.info("Data updated !!")
        cursor_server.close()
        connection_data.close()
    except Exception as e:
        logging.error(f"Error of saving data {e}")

schedule.every(1).minutes.do(automatise_data_save)

# Boucle principale
if __name__ == "__main__":
    print("🚀 Démarrage de sauvegarde des données from supabase (intervalle : 1 min)...")
    automatise_data_save()  # exécution initiale
    while True:
        schedule.run_pending()
        time.sleep(1)
