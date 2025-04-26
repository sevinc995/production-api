from flask import Flask, jsonify
from flask_cors import flask_cors
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

CORS(app)