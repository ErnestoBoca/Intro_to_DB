import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",      
        user="root",
        password="",
        database="alx_book_store"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

    cursor.close()
    conn.close()
except mysql.connector.Error as e:
    print("Error connecting to database", e)

        