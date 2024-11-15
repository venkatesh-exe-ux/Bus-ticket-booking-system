from tkinter import *
from PIL import ImageTk, Image
from ticket_booking import ticket_app
from passenger_details import details

def main_app():
    root = Tk()
    root.title("Red Bus")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    same = True
    n = 0.25

    background_image = Image.open("Bus.jpeg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FF0000", bd=2)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.26)

    headingLabel = Label(headingFrame1, text="Welcome to \n Redbus", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Book ticket", bg='black', fg='white', command=ticket_app)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="View Passenger Details", bg='black', fg='white', command=details)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    root.mainloop()
