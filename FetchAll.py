import csv
from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

def FetchAllDataCSV(filename="StudentDB.csv"):
    ClearScreen()
    try:
        con, cur = ConnectDB()

        cur.execute("SELECT * FROM INFO")
        records = cur.fetchall()

        if not records:
            print("No records found in database !")
            return

        column_names = [i[0] for i in cur.description]

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(column_names)
            writer.writerows(records)

        print(f"DATA EXPORTED IN CSV FILE - '{filename}'")
        print("-"*45)

    except Error as e:
        print("ERROR:", e)