from tkinter import *
from tkinter import messagebox
import json

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char


def newpass():
    input3.insert(0, password)

def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 and len(password) == 0:
        messagebox.askokcancel(title="Oops", message="Please do not leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input1.delete(0, END)
            input3.delete(0, END)

def new_search():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 and len(password) == 0:
        messagebox.askokcancel(title="Oops", message="Please do not leave any field empty")
    else:
        try:
            value = input1.get()
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                messagebox.askokcancel(title= value, message=f"Email: {data[value]['email']}  Password: {data[value]['password']}")
                messagebox.askyesno()
        except KeyError:
            result = messagebox.askyesno(title=value, message="Website not save. Want to save?")
            if result == True:
                messagebox.askokcancel(title=value, message="Enter a password!!")
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img= PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(column=1, row=0)


label = Label(text="Website: ")
label.grid(column=0, row=1)
input1 = Entry(width=23)
input1.grid(column=1, row=1)
input1.focus()

button_search = Button(text= "Search", width= 15, command= new_search)
button_search.grid(column=2, row=1)


label1 = Label(text="Email/Username: ")
label1.grid(column=0, row=2)
input2 = Entry(width=41)
input2.grid(column=1, row=2,columnspan=2)
input2.insert(0,"rahulk2903@gmail.com")


label2 = Label(text="Password: ")
label2.grid(column=0, row=3)
input3 = Entry(width=23)
input3.grid(column=1, row=3)

button1 = Button(text="Generate Password", width=15, command = newpass)
button1.grid(column=2, row=3)
button = Button(text="Add", width=35, command=save)
button.grid(column=1, row=4, columnspan=2)
window.mainloop()


