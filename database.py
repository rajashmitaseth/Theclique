from dbconnection import DBConnection as db
import pandas as pd

def createDatabase():
    cursor = db.getcursor()
    cursor.execute("CREATE DATABASE waterdata;")
    db.save()

def createTable():
    cursor = db.getcursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS water_quality (id SERIAL PRIMARY KEY, place VARCHAR(100), ph FLOAT, tds FLOAT, hardness FLOAT, nitrate FLOAT);")
    db.save()

def showTable():
    cursor = db.getcursor()
    cursor.execute("SELECT * FROM water_quality")
    all_districts_raw = cursor.fetchall()
    all_districts = []
    for district in all_districts_raw:
        all_districts.append(district)
    return all_districts

def search(criteria):
    cursor = db.getcursor()
    cursor.execute(f"SELECT * FROM water_quality WHERE {criteria}")
    all_results_raw = cursor.fetchall()
    all_results = []
    for result in all_results_raw:
        all_results.append(result)
    return all_results

createDatabase()