import pymysql

# Database connection parameters
db_params = {
    'host': 'localhost',
    'user': 'root',
    'password': ''  # Add your MySQL root password if you have one
}

try:
    # Connect to MySQL server
    connection = pymysql.connect(**db_params)
    
    try:
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS flask_auth_db")
            print("Database 'flask_auth_db' created successfully!")
    
    finally:
        connection.close()

except Exception as e:
    print(f"Error: {e}") 