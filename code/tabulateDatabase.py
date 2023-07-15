# Completely copied from chatGPT

import sqlite3
from tabulate import tabulate

# Connect to the database
connection = sqlite3.connect("database/database.db")

# Create a cursor
cursor = connection.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM employees")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Get the column names from the cursor description
columns = [desc[0] for desc in cursor.description]

# Print the result as a formatted table
print(tabulate(rows, headers=columns, tablefmt="grid"))

# Close the connection
connection.close()
