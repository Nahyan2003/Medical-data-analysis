import mysql.connector
import pandas as pd

# Connect to database
conn = mysql.connector.connect(
    host="18.136.157.135",
    port=3306,
    user="dm_team4",
    password="DM!$!Team!47@4!23&",
    database="project_medical_data_history"
)

print("Connected successfully!")

# Get list of all tables
cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

print("Tables found:", tables)

# Download each table as CSV
for table in tables:
    table_name = table[0]
    print(f"Downloading {table_name}...")

    df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
    df.to_csv(f"{table_name}.csv", index=False)

print("All tables downloaded successfully!")

conn.close()