import requests
from tkinter import *
from PIL import ImageTk, Image

api_url = 'https://quoteapi.pythonanywhere.com/random'
quote = ""
author = ""

def change_quote():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        quote = data["Quotes"][0]["quote"]
        author = data["Quotes"][0]["author"]
        canvas.itemconfig(canvas_text, text=f"{quote}")
        label_author.config(text=f"{author}")
    else:
        print('Failed to fetch data from API:', response.status_code)    


root = Tk()
root.title("Movie Quotes")
root.config(padx=50, pady=15)
canvas = Canvas(root, width=500, height=500)
img = ImageTk.PhotoImage(Image.open("movie_quote/background.png"))
canvas.create_image(250, 250, image=img)
canvas.grid(column=0, row=0)

canvas_text = canvas.create_text(250, 200, text="quote", font=("Ariel", 20, "italic"), width=250)

label_author = Label(text="author", font=("Ariel", 20, "italic"))
label_author.grid(column=0, row=1)
button_next = Button(text="Next Quote ->", font=("Ariel", 30, "bold"), command=change_quote)
button_next.grid(column=0, row=2)

change_quote()
root.mainloop()