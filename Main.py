from AddData import AddStudent
from Remove import RemoveStudent
from Update import UpdateStudent
from FetchData import FetchStudent
from FetchAll import FetchAllDataCSV
from MakeDB import CreateTable, ConnectDB
from Access import Login, Register, ViewAllUsers
from Reset import ResetMenu
from config import ClearScreen

# Initialize Database
def InitDB():
    try:
        con, cur = ConnectDB()
        CreateTable(cur, con)
    except:
        pass

# Login / Register Menu
def AuthMenu():
    while True:
        print("-"*45)
        print("- - STUDENT MANAGEMENT SYSTEM - -")
        print("-"*45)
        print("1. LOGIN")
        print("2. REGISTER NEW USER")
        print("3. EXIT")
        print("-"*45)
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            ClearScreen()
            success, role = Login()
            if success:
                ClearScreen()
                return role
        elif choice == "2":
            ClearScreen()
            Register()
            ClearScreen()
        elif choice == "3":
            print("-"*45)
            print("EXITED ~")
            exit()
        else:
            print("-"*45)
            print("Invalid Choice!")
            ClearScreen()

# Main Menu after Login
def MainMenu(role):
    while True:
        print("-"*45)
        print("- - - - STUDENTS MANAGEMENT SYSTEM - - - -")
        print("-"*45)
        print("1. ADD STUDENT DATA")
        print("2. FETCH STUDENT DATA")
        print("3. UPDATE STUDENT DATA")
        print("4. REMOVE STUDENT DATA")
        print("5. FETCH All STUDENT DATA")
        
        if role == "Admin":
            print("6. VIEW ALL USERS (Admin Only)")
            print("7. RESET DATABASE (Admin Only)")
            print("8. LOGOUT")
        else:
            print("6. LOGOUT")
        
        print("-"*45)

        if role == "Admin":
            choice = input("Enter your choice (1-8): ")
        else:
            choice = input("Enter your choice (1-6): ")
        
        ClearScreen()

        if choice == "1":
            AddStudent()
        elif choice == "2":
            FetchStudent()
        elif choice == "3":
            UpdateStudent()
        elif choice == "4":
            RemoveStudent()
        elif choice == "5":
            FetchAllDataCSV()
        elif choice == "6":
            if role == "Admin":
                ViewAllUsers()
            else:
                print("Logged Out Successfully!")
                break
        elif choice == "7" and role == "Admin":
            ResetMenu()
        elif choice == "8" and role == "Admin":
            print("Logged Out Successfully!")
            break
        else:
            print("Invalid Choice !")

        again = input("\nDo you want to continue ? (y/n): ").lower()
        if again == "n":
            ClearScreen()
            print("Logged Out Successfully!")
            break
        ClearScreen()

# Start Program
if __name__ == "__main__":
    InitDB()
    ClearScreen()
    while True:
        user_role = AuthMenu()
        MainMenu(user_role)
        ClearScreen()