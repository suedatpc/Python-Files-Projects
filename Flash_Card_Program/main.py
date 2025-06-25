from tkinter import *
from PIL import ImageTk, Image
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
data = pandas.read_csv("Flash_Card_Program/words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}


def change_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    root.after(3000, flip_card)
    incorrect_button.grid_remove()
    correct_button.grid_remove()




def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="Turkish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="white")
    incorrect_button.grid()
    correct_button.grid()
    



#UI Setup
root = Tk()
root.title("English/Turkish Flash Card Game")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_front = PhotoImage(file="Flash_Card_Program/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_back  = PhotoImage(file="Flash_Card_Program/images/card_back.png")

card_title = canvas.create_text(400, 150, font=LANG_FONT, text="lang")
card_word = canvas.create_text(400, 263, font=WORD_FONT, text="Word")


incorrect_img = PhotoImage(file="Flash_Card_Program/images/wrong.png")
correct_img = PhotoImage(file="Flash_Card_Program/images/right.png")

incorrect_button = Button(image=incorrect_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, activebackground=BACKGROUND_COLOR, command=change_card)
correct_button = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, activebackground=BACKGROUND_COLOR, command=change_card)
incorrect_button.grid(column=0, row=1)
correct_button.grid(column=1, row=1)


change_card()



root.mainloop()