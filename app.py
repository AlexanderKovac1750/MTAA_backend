from flask import Flask, request
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

@app.get("/login")
def try_to_login():
    name = request.args.get('name')
    password = request.args.get('password')
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public'  -- Change if you're using a different schema
        ORDER BY table_name;
    """)
    tables=cursor.fetchall()
    print(name, password)
    return {"stores": tables}

@app.post("/fav")
def add_fav():
    food = request.args.get('food')
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public'  -- Change if you're using a different schema
        ORDER BY table_name;
    """)
    tables=cursor.fetchall()
    print("new fav ",food)
    return {"stores": tables}

@app.delete("/fav")
def del_fav():
    food = request.args.get('food')
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public'  -- Change if you're using a different schema
        ORDER BY table_name;
    """)
    tables=cursor.fetchall()
    print("del fav ",food)
    return {"stores": tables}

@app.put("/preferences")
def change_settings():
    setting = request.args.get('setting')
    val = request.args.get('val')
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public'  -- Change if you're using a different schema
        ORDER BY table_name;
    """)
    tables=cursor.fetchall()
    print(f"changed {setting} to {val}")
    return {"stores": tables}

app.run()
