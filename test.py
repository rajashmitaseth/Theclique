# import psycopg2
# import pandas as pd
import csv
# import openpyxl
import gui

# connection = psycopg2.connect(
#     host = "localhost",
#     user = "postgres",
#     database = "waterdata",
#     password = "2006",
#     port = 5432
# )

# cursor = connection.cursor()

# #statements
# # cursor.execute("CREATE DATABASE waterdata;")
# cursor.execute("CREATE TABLE IF NOT EXISTS water_quality (id SERIAL PRIMARY KEY, place VARCHAR(100), ph VARCHAR(100), tds VARCHAR(100), hardness VARCHAR(100), nitrate VARCHAR(100));")

# table = pd.read_sql("SELECT * FROM water_quality;", connection)
# print(table)

# import requests

# url = "https://aikosha-api.indiaai.gov.in/akp/idp/api/v1/dataset-public/download-dataset?datasetIdentifier=jjm_water_source_water_quality_data&versionNumber=1'"
# response = requests.get(url)

# if response.status_code != 200:
#     print("Failed to fetch data.")
#     exit(1)

# data = response.json()

# for row in data:
#     print(row)
#     for a in row:
#         print(a)
    # cursor.execute("INSERT INTO water_quality (place,ph,tds,hardness,nitrate) VALUES (%s,%s,%s,%s,%s)", (
    #     row.get("DistrictName"),
    #     row.get("PH tested value (NA)"),
    #     row.get("TDS tested value (mg/l)"),
    #     row.get("Nitrate tested value (mg/l)")
    # ))

def findMatch(location):
    with open('book2.csv', mode='r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[3] == location:
                print(row)
            #print(', '.join(row))
        
#not working
# path = "book1.xlsx"
# wb = openpyxl.load_workbook(path)
# sheet = wb.active
# cells = sheet['A1':'X16976']
# for i in range(1, 16976):
#     cell = sheet.cell(row=i, column=j)
    
# for j in range(1,24):
#     cell = sheet.cell(row=i, column=j)
#     print(cell)

# connection.commit()

# cursor.close()
# connection.close()
