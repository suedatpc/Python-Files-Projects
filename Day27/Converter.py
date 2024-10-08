from tkinter import *
window = Tk()
window.title("Converter")
window.minsize(width=500, height=200)
window.config(padx=25, pady=30)


def reset():
    result_label.config(text="0")
    input.delete(0, END)   
    listbox.selection_clear(0, END)
    input.focus()
    label.config(text="")
    label2.config(text="")

def miles_to_km():
    label.config(text="Miles")
    label2.config(text="Km")
    result = round(float(input.get()) * 1.609, 3)
    result_label.config(text=f"{result}")

def km_to_miles():
    label.config(text="Km")
    label2.config(text="Miles")
    result = round(float(input.get()) / 1.609, 3)
    result_label.config(text=f"{result}")
 

input = Entry(width=8)
input.focus()
input.grid(column=2, row=0, sticky="W")

label = Label(text="")
label.grid(column=3, row=0, sticky="W")
label.config(padx=20)

equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1, sticky="W")
equal_label.config(pady = 20)

result_label = Label(text="0")
result_label.grid(column=1, row=1, sticky="W")
result_label.config(padx=20, pady=20)

label2 = Label(text="")
label2.grid(column=2, row=1, sticky="W")
label2.config(padx=-20)



conversions_dict = {
    "Miles to Kilometer": miles_to_km,
    "Kilometer to Miles": km_to_miles,
}

def listbox_used(event):
    selection = listbox.curselection()
    if selection:
        conversion = conversions_dict[listbox.get(selection)]
        conversion()



listbox = Listbox(height=2)
listbox.grid(column=3, row=1)

for item in conversions_dict:
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", listbox_used)


reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2, sticky="EW")



window.mainloop()