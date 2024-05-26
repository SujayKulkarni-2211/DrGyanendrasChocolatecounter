import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from PIL import Image, ImageTk
import csv

# Database Initialization
def init_db():
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    # Create table for leaderboard
    cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, chocolates INTEGER)''')

    connection.commit()
    connection.close()

# Function to search for a name and add to leaderboard if not found
def search_and_add(name):
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM leaderboard WHERE name=?", (name,))
    result = cursor.fetchone()
    if result:
        add_chocolates(result[0])
    else:
        chocolates = int(chocolates_entry.get())
        cursor.execute("INSERT INTO leaderboard (name, chocolates) VALUES (?, ?)", (name, chocolates))
        connection.commit()
        messagebox.showinfo("Success", f"Added {chocolates} chocolates to {name}")

    connection.close()

# Function to add chocolates to a name
def add_chocolates(name_id):
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    chocolates = int(chocolates_entry.get())
    cursor.execute("UPDATE leaderboard SET chocolates = chocolates + ? WHERE id=?", (chocolates, name_id))
    connection.commit()
    messagebox.showinfo("Success", f"Added {chocolates} chocolates to {search_entry.get()}")

    connection.close()

# Function to display leaderboard
def display_leaderboard():
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM leaderboard ORDER BY chocolates DESC")
    rows = cursor.fetchall()

    leaderboard_window = tk.Toplevel(root)
    leaderboard_window.title("Leaderboard")

    # Create a Treeview widget
    leaderboard_tree = ttk.Treeview(leaderboard_window, columns=("Name", "Chocolates"), show="headings")
    leaderboard_tree.heading("Name", text="Name")
    leaderboard_tree.heading("Chocolates", text="Chocolates")

    # Insert leaderboard data into the Treeview
    for row in rows:
        leaderboard_tree.insert("", "end", values=(row[1], row[2]))

    # Add Treeview to window
    leaderboard_tree.pack(fill="both", expand=True)

    connection.close()

# Function to search for a name and return corresponding chocolates
def search_and_return_chocolates(name):
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    cursor.execute("SELECT chocolates FROM leaderboard WHERE name=?", (name,))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Chocolates", f"{name} has {result[0]} chocolates.")
    else:
        messagebox.showinfo("Chocolates", f"{name} not found in the leaderboard.")

    connection.close()

# Function to export leaderboard data to CSV file
def export_to_csv():
    connection = sqlite3.connect('chocolate_counter.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM leaderboard ORDER BY chocolates DESC")
    rows = cursor.fetchall()

    with open("leaderboard.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Chocolates"])
        csv_writer.writerows(rows)

    messagebox.showinfo("Export Complete", "Leaderboard data exported to leaderboard.csv.")

    connection.close()

# Main GUI Setup
root = tk.Tk()
root.title("Dr. Gyanendra's Chocolate Counter")

init_db()

# Load and display image of Gyanendra sir
image = Image.open("CachhUP.png")
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, columnspan=3, pady=10)

# Slogan label
slogan_label = tk.Label(root, text="Encouraging Learning Every Day")
slogan_label.grid(row=1, column=0, columnspan=3, pady=5)

# Entry widget for searching names
search_label = tk.Label(root, text="Search for a name:")
search_label.grid(row=2, column=0, padx=5)
search_entry = tk.Entry(root)
search_entry.grid(row=2, column=1, padx=5)
search_button = tk.Button(root, text="Search", command=lambda: search_and_return_chocolates(search_entry.get().strip()))
search_button.grid(row=2, column=2, padx=5)

# Entry widget for adding chocolates
chocolates_label = tk.Label(root, text="No. of Chocolates:")
chocolates_label.grid(row=3, column=0, padx=5)
chocolates_entry = tk.Entry(root)
chocolates_entry.grid(row=3, column=1, padx=5)
chocolates_entry.insert(0, "1")  # Set default value
plus_button = tk.Button(root, text="+", font=("Arial", 20), command=lambda: search_and_add(search_entry.get().strip()))
plus_button.grid(row=3, column=2, padx=5)

# Button to display leaderboard
show_leaderboard_button = tk.Button(root, text="Show Leaderboard", command=display_leaderboard)
show_leaderboard_button.grid(row=4, column=0, columnspan=3, pady=10)

# Button to export leaderboard data to CSV
export_csv_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_csv_button.grid(row=5, column=0, columnspan=3, pady=5)

root.mainloop()
