from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Add Student Data To DB !

def AddStudent():
    ClearScreen()
    
    try:
        CCode = int(input("Enter Computer Code: "))
        FName = input("Enter First Name: ")
        LName = input("Enter Last Name: ")
        AGE = int(input("Enter Age: "))
        Class = int(input("Enter Class: "))
        SEC = input("Enter Section (A/B/C...): ")
        DOB = input("Enter DOB (YYYY-MM-DD): ")
        DName = input("Enter Full Father Name: ")
        MName = input("Enter Full Mother Name: ")
        Contact = int(input("Enter Contact Number (10 Digits only): "))
        Address = input("Enter Address (can include numbers and text): ")
        BNo = int(input("Enter Bus No: "))
        
        SECTION = SEC.upper()
        
        con, cur = ConnectDB()
        
        Query = f"INSERT INTO INFO VALUES ({CCode}, '{FName}', '{LName}', {AGE}, {Class},\
            '{SECTION}', '{DOB}', '{DName}', '{MName}', {Contact}, '{Address}', '{BNo}')"

        cur.execute(Query)
        con.commit()
        print("="*45)
        print("- - Data Added Successfully- -")
        print("="*45)
        
        cur.close()
        con.close()
        
    except Error as e:
        print("ERROR:", e)
        if 'con' in locals():
            con.rollback()
            cur.close()
            con.close()
    except ValueError:
        print("Invalid Input")
    except Exception as e:
        print(f"Unexpected Error: {e}")