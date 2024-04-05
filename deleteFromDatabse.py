import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
c = conn.cursor()

# Delete all data from the table
c.execute('''DELETE FROM quiz''')

# Commit changes and close connection
conn.commit()
conn.close()

# Print statement indicating data deletion
print("All data deleted from the database")
