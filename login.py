from tkinter import *
import pymysql
from tkinter import messagebox
from main_app import main_app

conn = pymysql.connect(host="localhost", user="root", password="admin@123", database="route")
cursor = conn.cursor()

def show_register():
    login_frame.pack_forget()
    register_frame.pack()

def show_login():
    register_frame.pack_forget()
    login_frame.pack()

def register_user():
    username = register_username_entry.get()
    password = register_password_entry.get()

    try:
        cursor.execute("INSERT INTO rose (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful! Please log in.")
        show_login()
    except pymysql.MySQLError as err:
        messagebox.showerror("Error", f"Error: {err}")

def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    cursor.execute("SELECT * FROM rose WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        root.destroy()
        main_app()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

root = Tk()
root.title("Jahnvi Bus")
root.geometry("600x500")

login_frame = Frame(root)
Label(login_frame, text="Username").pack()
login_username_entry = Entry(login_frame)
login_username_entry.pack()
Label(login_frame, text="Password").pack()
login_password_entry = Entry(login_frame, show='*')
login_password_entry.pack()
Button(login_frame, text="Login", command=login_user).pack()
Button(login_frame, text="Go to Register", command=show_register).pack()

register_frame = Frame(root)
Label(register_frame, text="Username").pack()
register_username_entry = Entry(register_frame)
register_username_entry.pack()
Label(register_frame, text="Password").pack()
register_password_entry = Entry(register_frame, show='*')
register_password_entry.pack()
Button(register_frame, text="Register", command=register_user).pack()
Button(register_frame, text="Go to Login", command=show_login).pack()

login_frame.pack()
root.mainloop()
