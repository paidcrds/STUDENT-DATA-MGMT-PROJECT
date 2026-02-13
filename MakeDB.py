import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Connect Without Database !

def CreateDatabase():
    try:
        con = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )      
        cur = con.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    finally:
        if con.is_connected():
            cur.close()
            con.close()

# Connect With Database !

def ConnectDB():

    con = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        
    cur = con.cursor()

    return con, cur

# Create Table in Database !

def CreateTable(cur, con):
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS INFO(
            ComCode INT PRIMARY KEY,
            FirstName VARCHAR(30),
            LastName VARCHAR(30),
            Age INT,
            Class INT(2),
            Section CHAR(1),
            Dob DATE,
            FatherName VARCHAR(50),
            MotherName VARCHAR(50),
            Contact BIGINT CHECK (Contact BETWEEN 1000000000 AND 9999999999),
            Address VARCHAR(100),
            BusNo VARCHAR(10)
        );
        """)
        
        # Create Users Table for Authentication
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ID(
            UserID INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(50) UNIQUE NOT NULL,
            Password VARCHAR(255) NOT NULL,
            FullName VARCHAR(100),
            Role VARCHAR(20) DEFAULT 'Staff'
        );
        """)
        
        con.commit()
    finally:
        cur.close()
        con.close()

CreateDatabase()