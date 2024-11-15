import tkinter as tk
from PIL import ImageTk, Image

def get_ticket_price(from_location, to_location):
    routes = {
        ('chennai', 'coimbatore'): 600,
        ('coimbatore', 'chennai'): 600,
        ('chennai', 'bangalore'): 800,
        ('bangalore', 'chennai'): 800,
        ('bangalore', 'hyderabad'): 1000,
        ('hyderabad', 'bangalore'): 1000,
        ('cochin', 'coimbatore'): 500,
        ('coimbatore', 'cochin'): 500,
        ('coimbatore', 'bangalore'): 900,
        ('bangalore', 'coimbatore'): 900,
        ('coimbatore', 'hyderabad'): 1200,
        ('hyderabad', 'coimbatore'): 1200,
        ('chennai', 'cochin'): 700,
        ('cochin', 'chennai'): 700,
        ('bangalore', 'cochin'): 1100,
        ('cochin', 'bangalore'): 1100,
        ('hyderabad', 'cochin'): 1300,
        ('cochin', 'hyderabad'): 1300
    }
    
    return routes.get((from_location, to_location), 0)

def calculate_ticket():
    from_location = from_var.get()
    to_location = to_var.get()
    persons = persons_entry.get()
    
    if not persons.isdigit():
        ticket_amount_label.config(text="Please enter a valid number of persons")
        return
    
    ticket_price = get_ticket_price(from_location, to_location)
    if ticket_price == 0:
        ticket_amount_label.config(text="Invalid route")
    else:
        total_amount = int(persons) * ticket_price
        ticket_amount_label.config(text=f"Ticket Amount: ${total_amount}")

def ticket_app():
    root = tk.Tk()
    root.title("Ticket Booking")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    background_image = Image.open("Bus.jpeg")
    image_size_width, image_size_height = background_image.size

    scale = 0.25
    new_image_size_width = int(image_size_width * scale)
    new_image_size_height = int(image_size_height * scale)

    background_image = background_image.resize((new_image_size_width, new_image_size_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(background_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    instructions_label = tk.Label(root, text="Select 'From' and 'To' locations to book a ticket:", bg='white')
    instructions_label.pack(pady=10)

    from_var = tk.StringVar(root)
    from_var.set('Select From Location')  

    to_var = tk.StringVar(root)
    to_var.set('Select To Location')

    from_locations = ['chennai', 'coimbatore', 'bangalore', 'hyderabad', 'cochin']
    from_menu = tk.OptionMenu(root, from_var, *from_locations)
    from_menu.pack(pady=10)

    to_menu = tk.OptionMenu(root, to_var, *from_locations)
    to_menu.pack(pady=10)

    tk.Label(root, text="Number of persons", bg='white').pack(pady=5)
    persons_entry = tk.Entry(root)
    persons_entry.pack(pady=5)

    calculate_button = tk.Button(root, text="Calculate Ticket Amount", command=calculate_ticket)
    calculate_button.pack(pady=10)

    ticket_amount_label = tk.Label(root, text="Ticket Amount: $0", bg='white')
    ticket_amount_label.pack(pady=10)

    root.mainloop()
