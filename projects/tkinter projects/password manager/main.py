from tkinter import *
from tkinter import messagebox
import string
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    letter = list(string.ascii_letters)
    number = list(range(10))
    symbol = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]
    password_letters = [choice(letter) for _ in range(randint(8, 10))]
    password_numbers = [choice(number) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbol) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    new_password = ""
    for char in password_list:
        new_password += str(char)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)  # copying thing in clipboard


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Data for {website} Found!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any field empty. ")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="#9BA4B5")

canvas = Canvas(width=200, height=200, bg="#9BA4B5", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# ---------------------- Labels ------------------------- #
website_label = Label(text="Website:", bg="#9BA4B5")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg="#9BA4B5")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="#9BA4B5")
password_label.grid(row=3, column=0)

# ---------------------- Entries ------------------------- #
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=38)
password_entry.grid(row=3, column=1, columnspan=2)
# ---------------------- Buttons ------------------------- #
search_button = Button(text="Search", command=find_password, width=14, activebackground="#05BFDB", bd=0)
search_button.grid(row=1, column=3)

pass_generator_button = Button(text="Generate Password", command=password_generator, activebackground="#05BFDB", bd=0)
pass_generator_button.grid(row=3, column=3)

add_button = Button(text="Add", width=34, command=save, activebackground="#05BFDB")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
