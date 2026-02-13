from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Register New User
def Register():
    try:
        print("-"*45)
        print("- - - - REGISTRATION FORM - - - -")
        print("-"*45)
        
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        confirm_password = input("Confirm Password: ")
        
        if password != confirm_password:
            print("Passwords do not match!")
            return False
        
        fullname = input("Enter Full Name: ")
        role = input("Enter Role (Admin/Teacher/Staff): ").capitalize()
        
        if role not in ["Admin", "Teacher", "Staff"]:
            print("Invalid Role! Choose Admin, Teacher, or Staff")
            return False
        
        con, cur = ConnectDB()
        
        # Check if username already exists
        cur.execute("SELECT * FROM ID WHERE Username = %s", (username,))
        if cur.fetchone():
            print("Username already exists! Choose another.")
            return False
        
        query = "INSERT INTO ID (Username, Password, FullName, Role) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (username, password, fullname, role))
        con.commit()
        
        print("-"*45)
        print("Registration Successful!")
        print("-"*45)
        return True
        
    except Error as e:
        print("ERROR:", e)
        return False
    finally:
        if con.is_connected():
            cur.close()
            con.close()

# Login User
def Login():
    try:
        print("-"*45)
        print("- - - - LOGIN FORM - - - -")
        print("-"*45)
        
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        con, cur = ConnectDB()
        
        query = "SELECT * FROM ID WHERE Username = %s AND Password = %s"
        cur.execute(query, (username, password))
        user = cur.fetchone()
        
        if user:
            return True, user[4]  # Return success and role
        else:
            print("-"*45)
            print("Invalid Username or Password.")
            print("-"*45)
            return False, None
            
    except Error as e:
        print("ERROR:", e)
        return False, None
    finally:
        if con.is_connected():
            cur.close()
            con.close()

# View All Users (Admin only)
def ViewAllUsers():
    try:
        con, cur = ConnectDB()
        
        cur.execute("SELECT UserID, Username, Password, FullName, Role FROM ID")
        users = cur.fetchall()
        
        if not users:
            print("No users found!")
            return
        
        print("-"*90)
        print("- - - - ALL REGISTERED USERS - - - -")
        print("-"*90)
        for user in users:
            print(f"ID: {user[0]} | Username: {user[1]} | Password: {user[2]} | Name: {user[3]} | Role: {user[4]}")
        print("-"*90)
        
    except Error as e:
        print("ERROR:", e)
    finally:
        if con.is_connected():
            cur.close()
            con.close()