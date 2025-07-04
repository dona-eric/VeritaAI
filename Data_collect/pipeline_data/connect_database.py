import psycopg2, os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor_server = connection.cursor()
    
    # Example query
    cursor_server.execute("""
                          CREATE TABLE news(
                          id SERIAL PRIMARY KEY,
                          title TEXT,
                          description TEXT,
                          author TEXT,
                          content TEXT,
                          published_at TIMESTAMP,
                          source TEXT,
                          category TEXT);
                          """)
    # fetch if table already exists
    cursor_server.execute("""
                          SELECT EXISTS(
                          SELECT FROM information_schema.tables
                          WHERE table_name='news');
                        """)
    #tables  = cursor_server.fetchall()
    #[t[0] for t in tables]    
    exists_table = cursor_server.fetchone()[0]
    if exists_table:
        print("Successful table create")
    else:
        print("Error")
    # Close the cursor and connection
    cursor_server.close()
    connection.close()
    #print("Table news créée avec succès dans Supabase.")
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")