from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Reset INFO Table (Student Records)
def ResetINFO():
    ClearScreen()
    try:
        confirm = input("Are you sure you want to DELETE ALL STUDENT RECORDS? (yes/no): ").lower()
        
        if confirm == "yes":
            con, cur = ConnectDB()
            
            cur.execute("DELETE FROM INFO")
            con.commit()
            
            print("-"*45)
            print("✓ All Student Records Deleted Successfully!")
            print("-"*45)
            
            cur.close()
            con.close()
        else:
            print("Reset Cancelled.")
            
    except Error as e:
        print("ERROR:", e)

# Reset ID Table (User Accounts)
def ResetID():
    ClearScreen()
    try:
        confirm = input("Are you sure you want to DELETE ALL USER ACCOUNTS? (yes/no): ").lower()
        
        if confirm == "yes":
            con, cur = ConnectDB()
            
            cur.execute("DELETE FROM ID")
            con.commit()
            
            print("-"*45)
            print("✓ All User Accounts Deleted Successfully!")
            print("-"*45)
            
            cur.close()
            con.close()
        else:
            print("Reset Cancelled.")
            
    except Error as e:
        print("ERROR:", e)

# Reset Both Tables
def ResetALL():
    ClearScreen()
    try:
        confirm = input("Are you sure you want to DELETE ALL DATA (Students + Users)? (yes/no): ").lower()
        
        if confirm == "yes":
            con, cur = ConnectDB()
            
            cur.execute("DELETE FROM INFO")
            cur.execute("DELETE FROM ID")
            con.commit()
            
            print("-"*45)
            print("- Student Records: Cleared")
            print("- User Accounts: Cleared")
            print("-"*45)
            
            cur.close()
            con.close()
        else:
            print("Reset Cancelled.")
            
    except Error as e:
        print("ERROR:", e)

# Reset Menu
def ResetMenu():
    while True:
        ClearScreen()
        print("-"*45)
        print("- - - - DATABASE RESET MENU - - - -")
        print("-"*45)
        print("1. Reset INFO (Delete All Students)")
        print("2. Reset ID (Delete All Users)")
        print("3. Reset ALL (Delete Everything)")
        print("4. Back to Main Menu")
        print("-"*45)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            ResetINFO()
        elif choice == "2":
            ResetID()
        elif choice == "3":
            ResetALL()
        elif choice == "4":
            ClearScreen()
            print("Returning to Main Menu...")
            break
        else:
            print("-"*45)
            print("Invalid Choice!")
        
        input("\nPress Enter to continue...")
        ClearScreen()