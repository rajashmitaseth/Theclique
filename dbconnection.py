import psycopg2
import pandas as pd

class DBConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host = "localhost",
                user = "postgres",
                password = "2006",
                port = 5432
            )
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            exit(1)

    def close(self):
        self.connection.close()

    def getconnection(self):
        return self.connection
    
    def getcursor(self):
        return self.connection.cursor()
    
    def save(self):
        self.connection.commit()

    def show(self):
        table = pd.read_sql("SELECT * FROM water_quality;", self.connection)
        return table


# cursor = connection.cursor()

# #statements
# cursor.execute("CREATE DATABASE waterdata;")
# cursor.execute("CREATE TABLE IF NOT EXISTS water_quality (id SERIAL PRIMARY KEY, place VARCHAR(100), ph FLOAT, tds FLOAT, hardness FLOAT, nitrate FLOAT);")

# connection.commit()

# table = pd.read_sql("SELECT * FROM water_quality;", dbconnection)
# print(table)

# cursor.close()
# connection.close()
