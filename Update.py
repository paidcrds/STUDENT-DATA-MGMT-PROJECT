from MakeDB import ConnectDB
from mysql.connector import Error
from config import ClearScreen

# Update DataBase Info !

def UpdateStudent():
    ClearScreen()

    try:
        code = int(input("Enter Computer Code of Student to Update: "))

        con, cur = ConnectDB()
        cur.execute("SELECT * FROM INFO WHERE ComCode = %s", (code,))
        record = cur.fetchone()

        if not record:
            print("No student found with that Computer Code !")
            cur.close()
            con.close()
            return
        
        print("-"*45)
        print("- - - What do you want to Update ? - - -")
        print("-"*45)
        print("1. First Name")
        print("2. Last Name")
        print("3. Age")
        print("4. Class")
        print("5. Section")
        print("6. DOB")
        print("7. Father Name")
        print("8. Mother Name")
        print("9. Contact")
        print("10. Address")
        print("11. Bus No")
        print("-"*45)

        while True:
            choice = input("Enter Your Choice: ")
            print("-"*45)

            if choice == "1":
                field = "FirstName"
            elif choice == "2":
                field = "LastName"
            elif choice == "3":
                field = "Age"
            elif choice == "4":
                field = "Class"
            elif choice == "5":
                field = "Section"
            elif choice == "6":
                field = "Dob"
            elif choice == "7":
                field = "FatherName"
            elif choice == "8":
                field = "MotherName"
            elif choice == "9":
                field = "Contact"
            elif choice == "10":
                field = "Address"
            elif choice == "11":
                field = "BusNo"
            else:
                print("Invalid Choice !")
                continue
        
            try:
                if field == "FirstName":
                    print("Enter Student First Name ~")
                elif field == "LastName":
                    print("Enter Student Last Name ~")
                elif field == "Age":
                    print("Enter Student Age ( INTEGER ACCEPT ) ~")
                elif field == "Class":
                    print("Enter Student New Class ( INTEGER ACCEPT ) ~")
                elif field == "Section":
                    print("Enter Student New Section ( FORMAT - A/B/C... ) ~")
                elif field == "Dob":
                    print("Enter Student Dob ( FORMAT - YYYY-MM-DD ) ~")
                elif field == "FatherName":
                    print("Enter Student Father Name ~")
                elif field == "MotherName":
                    print("Enter Student Mother Name ~")    
                elif field == "Contact":
                    print("Enter 10 Digits number only ~")
                elif field == "Address":
                    print("Enter New Address ~")
                elif field == "BusNo":
                    print("Enter New BusNo ( INTEGER ACCEPT ) ~")

                NewValue = input(f"ENTER: {field} = ")

                query = f"UPDATE INFO SET {field} = %s WHERE ComCode = %s"
                cur.execute(query, (NewValue, code))
                con.commit()
                print("-"*45)
                print("- - - - Record Updated Successfully ! - - - -")
                print("-"*45)

                again = input("Do you want to update another field for this student ? (y/n): ").lower()
                if again == "n":
                    print("-"*45)
                    print("- - - - - - UPDATE MENU CLOSED - - - - - -")
                    print("-"*45)
                    break

            except ValueError:
                print("Invalid Input")
            except Exception as e:
                print("ERROR:", e)
            except Error as e:
                print("ERROR:", e)
        
        cur.close()
        con.close()
        
    except ValueError:
        print("Invalid Input!")
    except Error as e:
        print("ERROR:", e)
    except Exception as e:
        print("ERROR:", e)