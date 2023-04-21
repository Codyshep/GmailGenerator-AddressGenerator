import sqlite3
import tkinter as tk

# Initialize GUI
root = tk.Tk()
root.configure(background='black')
root.title("Database Display")

# Connect to SQLite database
conn = sqlite3.connect('fake_accounts.db')

# Create table for storing account information
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS accounts
            (email text, password text, first_name text, last_name text, address text)''')

# Retrieve account information from table
try:
    c.execute("SELECT * FROM accounts")
    accounts = c.fetchall()
except sqlite3.OperationalError:
    accounts = [("Error", "Table not found", "", "", "")]

# Create text box to display account information
textbox = tk.Text(root, bg="black", fg="white")
textbox.pack(pady=5)

# Display account information in text box
for account in accounts:
    textbox.insert(tk.END, f"Email: {account[0]}\n")
    textbox.insert(tk.END, f"Password: {account[1]}\n")
    textbox.insert(tk.END, f"First Name: {account[2]}\n")
    textbox.insert(tk.END, f"Last Name: {account[3]}\n")
    textbox.insert(tk.END, f"Address: {account[4]}\n")
    textbox.insert(tk.END, "-"*50 + "\n")

# Add border to text box
textbox.config(borderwidth=2, relief="solid")

# Run GUI loop
root.mainloop()

# Close connection to database
conn.close()
