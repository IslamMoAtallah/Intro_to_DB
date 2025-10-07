# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 8.0.43

import grt
#import mforms
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error :
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            # Optional: print confirmation of closure
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
