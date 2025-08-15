import mysql.connector

print("🚀 Starting MySQL connection test...")
print("⏳ Trying to connect...")

try:
    print("🛠 Attempting to connect with parameters...")
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='*Notebook@2025',
        database='30day_sql_query',
        connection_timeout=5
    )
    print("✅ Connected successfully")
    conn.close()
except mysql.connector.Error as err:
    print("❌ Connection failed:")
    print(err)
