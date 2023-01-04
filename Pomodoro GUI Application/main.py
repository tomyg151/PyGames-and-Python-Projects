from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
number_of_checkmarks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global number_of_checkmarks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")  # timer_text 00:00
    title_label.config(text="Timer")  # title_label "Timer"
    number_of_checkmarks = ""  # reset check_marks
    Check_mark_label.config(text=f"{number_of_checkmarks}")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        reps = 0
        title_label.config(text="Break", fg=RED)

    # if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    # if it's the 1st/3rd/5th/7th reps:
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global number_of_checkmarks
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            number_of_checkmarks += "✔"
            Check_mark_label.config(text=f"{number_of_checkmarks}", fg=GREEN)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# lable - page title
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)  # fg is for fill the text color
title_label.grid(row=0, column=2)

canvas = Canvas(width=200, height=230, bg=YELLOW,
                highlightthickness=0)  # put the canvas at the background of the window
tomato_img = PhotoImage(file="tomato.png")  # we must first to call to PhotoImage to
# read the file and only than we can use it
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# bottom start
button_start = Button(text="Start", bg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(row=3, column=0)

# Check mark label
Check_mark_label = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
Check_mark_label.grid(row=3, column=2)

# bottom reset
button_reset = Button(text="Reset", bg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
button_reset.grid(row=3, column=3)

window.mainloop()
