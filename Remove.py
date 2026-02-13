from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Remove Database Record !

def RemoveStudent():
    ClearScreen()
    
    try:
        code = int(input("Enter student code: "))
        
        con, cur = ConnectDB()
        cur.execute("SELECT * FROM INFO WHERE ComCode = %s", (code,))
        record = cur.fetchone()

        if record:
            confirm = input("Are you sure, you want to Delete Record ? (y/n): ").lower()
            if confirm == 'y':
                cur.execute("DELETE FROM INFO WHERE ComCode = %s", (code,))
                con.commit()
                print("Student Data Deleted Successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("No Data found with that Computer Code to Remove !")
        
        cur.close()
        con.close()

    except ValueError:
        print("Invalid Input !")
    except Error as e:
        print("ERROR:", e)
    except Exception as e:
        print("ERROR:", e)