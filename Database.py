import tkinter as tk
from tkinter import messagebox

# Fake database for demonstration
database = {}

def go_to_page(page_number):
    for page in pages:
        page.pack_forget()
    pages[page_number].pack()

def submit_page1():
    global first_name, last_name, email
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()

    if not first_name or not last_name or not email:
        messagebox.showerror("Error", "All fields are required!")
        return
    go_to_page(1)

def submit_page2():
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    database[first_name] = {'last_name': last_name, 'email': email, 'password': password}
    messagebox.showinfo("Success", "Registration successful!")
    go_to_page(2)

def login():
    username = entry_login_name.get()
    password = entry_login_password.get()

    if username in database and database[username]['password'] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Initialize the main window
root = tk.Tk()
root.title("Multi-page Form")

# Define pages
pages = [tk.Frame(root) for _ in range(3)]
for page in pages:
    page.pack(fill="both", expand=True)

# Page 1: User Info
label_first_name = tk.Label(pages[0], text="First Name")
label_first_name.pack()
entry_first_name = tk.Entry(pages[0])
entry_first_name.pack()

label_last_name = tk.Label(pages[0], text="Last Name")
label_last_name.pack()
entry_last_name = tk.Entry(pages[0])
entry_last_name.pack()

label_email = tk.Label(pages[0], text="Email")
label_email.pack()
entry_email = tk.Entry(pages[0])
entry_email.pack()

button_next = tk.Button(pages[0], text="Next", command=submit_page1)
button_next.pack()

# Page 2: Password Setup
label_password = tk.Label(pages[1], text="Password")
label_password.pack()
entry_password = tk.Entry(pages[1], show="*")
entry_password.pack()

label_confirm_password = tk.Label(pages[1], text="Confirm Password")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(pages[1], show="*")
entry_confirm_password.pack()

button_back = tk.Button(pages[1], text="Back", command=lambda: go_to_page(0))
button_back.pack()

button_submit = tk.Button(pages[1], text="Submit", command=submit_page2)
button_submit.pack()

# Page 3: Login
label_login_name = tk.Label(pages[2], text="First Name")
label_login_name.pack()
entry_login_name = tk.Entry(pages[2])
entry_login_name.pack()

label_login_password = tk.Label(pages[2], text="Password")
label_login_password.pack()
entry_login_password = tk.Entry(pages[2], show="*")
entry_login_password.pack()

button_login = tk.Button(pages[2], text="Login", command=login)
button_login.pack()

# Start on page 1
go_to_page(0)

root.mainloop()
