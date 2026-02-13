from AddData import AddStudent
from Remove import RemoveStudent
from Update import UpdateStudent
from FetchData import FetchStudent
from FetchAll import FetchAllDataCSV
from MakeDB import CreateTable, ConnectDB

con, cur = ConnectDB()
CreateTable(cur, con)

while True:
    print("-"*45)
    print("- - - - STUDENTS MANAGEMENT SYSTEM - - - -")
    print("-"*45)
    print("1. ADD STUDENT DATA")
    print("2. FETCH STUDENT DATA")
    print("3. UPDATE STUDENT DATA")
    print("4. REMOVE STUDENT DATA")
    print("5. FETCH All STUDENT DATA")
    print("6. EXIT PROGRAM")
    print("-"*45)

    choice = input("Enter your choice (1-6): ")
    print("-"*45)

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
        print("EXITED ~")
        break
    else:
        print("Invalid Choice !")

    again = input("Do you want to continue ? (y/n): ").lower()
    if again == "n":
        print("EXITED ~")
        break