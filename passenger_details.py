from tkinter import *
from tkinter import messagebox
import pymysql

def details():
    root = Tk()
    root.title("Passenger Details")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    con = pymysql.connect(host="localhost", user="root", password="admin@123", database="route")
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FF0000")
    Canvas1.pack(expand=True, fill=BOTH)
        
    headingFrame1 = Frame(root, bg="#00FF00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Passenger Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
    
    lb1 = Label(labelFrame, text="Username: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
        
    passInfo1 = Entry(labelFrame)
    passInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(labelFrame, text="Age: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
        
    passInfo2 = Entry(labelFrame)
    passInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame, text="From Location: ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
        
    passInfo3 = Entry(labelFrame)
    passInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
    
    lb4 = Label(labelFrame, text="To Location: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
        
    passInfo4 = Entry(labelFrame)
    passInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame, text="Mobile: ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.80, relheight=0.08)

    passInfo5 = Entry(labelFrame)
    passInfo5.place(relx=0.3, rely=0.75, relwidth=0.62, relheight=0.08)

    def submit_details():
        username = passInfo1.get()
        age = passInfo2.get()
        from_location = passInfo3.get()
        to_location = passInfo4.get()
        mobile = passInfo5.get()

        if not (username and age and from_location and to_location and mobile):
            messagebox.showerror("Error", "All fields are required")
            return

        insert_query = "INSERT INTO passenger_details (username, age, from_location, to_location, mobile) VALUES (%s, %s, %s, %s, %s)"
        try:
            cur.execute(insert_query, (username, age, from_location, to_location, mobile))
            con.commit()
            messagebox.showinfo('Success', "Details added successfully")
        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Can't add details into database: {e}")
        finally:
            root.destroy()

    SubmitBtn = Button(root, text="Submit", bg='#d1ccc0', fg='black', command=submit_details)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()
