from flask import Flask, request
app = Flask(__name__)
import psycopg2

connection = psycopg2.connect (
    database="allinonemd",
    user="mddbadmin",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS documents (id serial PRIMARY KEY, name varchar);")
connection.commit()
