from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Retrieve Student Data !

def FetchStudent():
    ClearScreen()
    
    try:
        code = int(input("Enter Computer Code of Student: "))

        con, cur = ConnectDB()
        cur.execute("SELECT * FROM INFO WHERE ComCode = %s", (code,))
        record = cur.fetchone()

        if not record:
            print("No Data found with that Computer Code !")
            cur.close()
            con.close()
            return

        print("-" * 40)
        print("Student Record Found ~")
        print("-" * 40)
        print(f"Computer Code : {record[0]}")
        print(f"First Name    : {record[1]}")
        print(f"Last Name     : {record[2]}")
        print(f"Age           : {record[3]}")
        print(f"Class         : {record[4]}")
        print(f"Section       : {record[5]}")
        print(f"DOB           : {record[6]}")
        print(f"Father Name   : {record[7]}")
        print(f"Mother Name   : {record[8]}")
        print(f"Contact No.   : {record[9]}")
        print(f"Address       : {record[10]}")
        print(f"Bus No        : {record[11]}")
        print("-" * 40)
        
        cur.close()
        con.close()

    except ValueError:
        print("Invalid Input !")
    except Error as e:
        print("ERROR:", e)