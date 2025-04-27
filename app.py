from flask import Flask, jsonify
from flask_cors import flask_cors
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

CORS(app)


def get_db_connection():

    try:
        conn = psycopg2.connect(
            host = os.getenv('PGHOST'),
            USE = OS.getenv('PGUSER'),
            database = os.getenv('PGDATABASE'),
            password = os.getenv('PGPASSWORD'),
            port = os.getenv('PGPORT')
            sslmode = 'require'
        )
    
        return conn

    except Exception as e:
        print(f"Database connection error: (e)")
        return None

@app.route("/api/news", methods=["GET"])
def get_news():


    try:
        conn = get_db_connection()

        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()

        cursor.execute("SELECT id, title, description, image FROM news")

        news = cursor.fetchall()

        cursor.close()

        conn.close()

        
