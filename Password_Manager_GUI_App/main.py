from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import choice, randint, shuffle
import json

#Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword():
    password_list = []
    entry_password.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)


#Save Password
def saveData():
    website = entry_website.get().lower()
    email_username = entry_email_username.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email" : email_username,
            "password" : password
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(message="Please don't leave any fields empty!")
    else:
        is_yes = messagebox.askyesno(message="Do you wish to save it?")
        if is_yes:
            try:
                with open("Password_Manager_GUI_App/password_data.json", mode="r") as data_file:
                    #read old data
                    data = json.load(data_file) 

                    if website in data:
                        update = messagebox.askyesno(title="Warning", message=f"There is already a password saved for {website}.\nWould you like to overwrite?")  
                        if update:
                            pass
                        else:
                            return

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data

            else:
                #update old data w new data
                data.update(new_data)

                with open("Password_Manager_GUI_App/password_data.json", mode="w") as data_file:
                    #write updated data
                    json.dump(data, data_file, indent=4)

            finally:    
                entry_website.delete(0, END)
                entry_email_username.delete(0, END)
                entry_password.delete(0, END)
                entry_website.focus()


#Search website
def searchPassword():
    website = entry_website.get().lower()
    if len(website) == 0:
        messagebox.showerror(title="Empty Field!", message="Enter a website to search")
    else:
        try:
            with open("Password_Manager_GUI_App/password_data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email/Username: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


#UI Setup
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=20)

canvas = Canvas(root, width=200, height=200)
img = ImageTk.PhotoImage(Image.open("Password_Manager_GUI_App/logo.png"))
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_email_username = Label(text="Email/Username:")
label_password = Label(text="Password:")
entry_website = Entry(width=35)
entry_email_username = Entry(width=35)
entry_password = Entry(width=25)
button_search = Button(root, text="Search", command=searchPassword)
button_generate = Button(root, text="Generate Password", command=generatePassword)
button_add = Button(root, text="Add", command=saveData)

label_website.grid(column=0, row=1, sticky="E")
label_email_username.grid(column=0, row=2, sticky="E")
label_password.grid(column=0, row=3, sticky="E")
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()
entry_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_password.grid(column=1, row=3, sticky="EW")
button_generate.grid(column=2, row=3, sticky="EW")
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")
button_search.grid(column=2, row=1, sticky="EW")

root.mainloop()
