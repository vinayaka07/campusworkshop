"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7m8rhp8u7g2edvj6g-a.oregon-postgres.render.com",
        database="todo_buhu",
        user="root",
        password="39Xk6Gst2K43tbLsCczEDu6IcdMLDuOC")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
