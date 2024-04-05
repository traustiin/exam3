import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
c = conn.cursor()

# Execute a query to check if the table is empty
c.execute('''SELECT COUNT(*) FROM quiz''')
row_count = c.fetchone()[0]

# Check if the table is empty
if row_count == 0:
    print("The database table is empty")
else:
    print("The database table is not empty")

# Close connection
conn.close()

