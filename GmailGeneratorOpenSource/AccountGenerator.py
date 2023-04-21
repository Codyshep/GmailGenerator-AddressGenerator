import sqlite3
import random
import string
import time
from faker import Faker
import tkinter as tk
from tkinter import filedialog

# Initialize GUI
root = tk.Tk()
root.configure(background='black')
root.title("Account Generator")

# Initialize default value of accountsGend
accountsGend = tk.IntVar()
accountsGend.set(5)

# Define function to update accountsGend
def update_accounts_gend():
    global accountsGend
    accountsGend = int(entry.get())
    root.quit()

# Define function to clear database
def clear_database():
    # Connect to SQLite database
    conn = sqlite3.connect('fake_accounts.db')

    # Drop accounts table
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS accounts''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Define function to export to TXT file
def export_to_txt():
    # Connect to SQLite database
    conn = sqlite3.connect('fake_accounts.db')

    # Retrieve account information from database
    c = conn.cursor()
    c.execute('''SELECT * FROM accounts''')
    rows = c.fetchall()

    # Open file dialog for saving file
    filename = filedialog.asksaveasfilename(initialdir='/', title='Save as', filetypes=[('Text files', '*.txt')])

    # Write account information to file
    with open(filename, 'w') as f:
        for row in rows:
            f.write(str(row) + '\n')

    # Close connection
    conn.close()

# Create label for text box
label = tk.Label(root, text="Enter number of accounts to generate:", fg="white", bg="black")
label.pack(pady=5)

# Create text box for accountsGend
entry = tk.Entry(root, textvariable=accountsGend, bg="black", fg="white")
entry.pack(pady=5)

# Create button to confirm accountsGend
button = tk.Button(root, text="Confirm", command=update_accounts_gend, bg="white", fg="black")
button.pack(pady=5)

# Create button to clear database
clear_button = tk.Button(root, text="Clear Database", command=clear_database, bg="white", fg="black")
clear_button.pack(pady=5)

# Create button to export to TXT file
export_button = tk.Button(root, text="Export to TXT", command=export_to_txt, bg="white", fg="black")
export_button.pack(pady=5)

# Run GUI loop
root.mainloop()

# Initialize Faker object
fake = Faker()

# Loop to generate accounts
for i in range(accountsGend):
    # Generate random email
    email = fake.user_name() + random.choice(["@gmail.com", "@yahoo.com"])

    # Generate random password
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

    # Generate fake first and last name
    first_name = fake.first_name()
    last_name = fake.last_name()

    # Generate fake address
    address = fake.address()

    # Connect to SQLite database
    conn = sqlite3.connect('fake_accounts.db')

    # Create table for storing account information
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                (email text, password text, first_name text, last_name text, address text)''')

    # Insert account information into table
    c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)", (email, password, first_name, last_name, address))

    # Commit changes and close connection
    conn.commit()
    conn.close()
