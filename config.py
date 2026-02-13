import os

# Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "maxton"
DB_NAME = "SchoolDB"

# Clear Screen Function
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')