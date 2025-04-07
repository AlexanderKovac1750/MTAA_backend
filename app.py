from flask import Flask
import psycopg2

app = Flask(__name__)


connection=psycopg2.connect(
    host="localhost",
    database="CV2",
    user="postgres",
    password="123"
    )
connection=psycopg2.connect(
"postgresql://postgres:123@localhost:5432/CV2"
)
cursor = connection.cursor()



stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]

@app.get("/store")
def get_stores():
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public'  -- Change if you're using a different schema
        ORDER BY table_name;
    """)
    tables=cursor.fetchall()
    return {"stores": tables}

app.run()
