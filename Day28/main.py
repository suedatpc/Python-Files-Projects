from tkinter import *
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
GRAY = "#4a4c4f"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
my_timer = NONE 
 # ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    start_button["state"] = "active"
    root.after_cancel(my_timer)
    canvas.itemconfig(timer, text= "00:00")
    checkmark.config(text="")
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1 
    start_button["state"] = "disabled"
    start_button["disabledforeground"] = start_button["foreground"]

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        break_label.config(fg=GRAY)
        root.bell()
        focus_window("on")
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        break_label.config(fg=GRAY)
        root.bell()
        focus_window("on")
    else:
        count_down(work_sec)
        break_label.config(fg="white")
        root.bell()
        focus_window("off")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #  
def count_down(count):
    count_min, count_sec = divmod(count, 60)
    canvas.itemconfig(timer, text=f"{count_min:02}:{count_sec:02}") #Here 0 is filler and 2 is the minimum width
    if count > 0:
        global my_timer
        my_timer = root.after(1000, count_down, count -1)
    else:
        start_timer()
        work_sessions = math.floor(REPS/2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)
            
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro Timer")
root.minsize(width=736, height=658)

bg_image = ImageTk.PhotoImage(Image.open("Day28/bg.gif"))


canvas = Canvas(root, width=736, height=658, background="white")
canvas.create_image(368, 329, image=bg_image)
timer = canvas.create_text(335, 260, text="00:00", fill=GRAY, font=(FONT_NAME, 45, "bold"))



start_button = Button(root, text="Start", command=start_timer, bg="white", highlightbackground="white")
reset_button = Button(root, text="Reset", command=reset_timer, bg="white", highlightbackground="white")

checkmark = Label(background="white", fg=GRAY)
break_label = Label(text="BREAK", background="white", fg="white")

def focus_window(option):
    if option == "on":
        root.deiconify()
        root.focus_force()
        root.attributes('-topmost', 1)
    elif option == "off":
        root.attributes('-topmost', 0)

canvas.pack()
canvas.create_window(334, 300, window=start_button)
canvas.create_window(334, 330, window=reset_button)
canvas.create_window(334, 500, window=checkmark)
canvas.create_window(335, 200, window=break_label)

start_button.config(font=(FONT_NAME, 15, "bold"))
reset_button.config(font=(FONT_NAME, 15, "bold"))
break_label.config(font=(FONT_NAME, 20, "bold"))
root.configure(bg="white")


root.mainloop()