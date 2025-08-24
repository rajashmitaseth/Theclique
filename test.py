import psycopg2
import pandas as pd


connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    database = "waterdata",
    password = "2006",
    port = 5432
)

cursor = connection.cursor()

#statements
# cursor.execute("CREATE DATABASE waterdata;")
cursor.execute("CREATE TABLE IF NOT EXISTS water_quality (id SERIAL PRIMARY KEY, place VARCHAR(100), ph FLOAT, tds FLOAT, hardness FLOAT, nitrate FLOAT);")

connection.commit()

table = pd.read_sql("SELECT * FROM water_quality;", connection)
print(table)

cursor.close()
connection.close()
