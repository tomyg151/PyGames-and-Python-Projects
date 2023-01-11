from tkinter import *
import random
import pandas
from tkinter import messagebox

from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
current_card_index = {}
to_learn = {}

# ---------------------------- READ CSV FILE ------------------------------- #
"""on the first time we run the program the words_to_learn file will not 
   exist that why we will use the original french_word file"""


def read_file():
    global to_learn
    try:
        data = pandas.read_csv("data/words_to_learn.csv")  # read csv file
    except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")  # read csv file
        to_learn = original_data.to_dict(orient='records')  # convert dataFrame to list with
        # many dictionary's of french word with translation in english
    except EmptyDataError:
        messagebox.showinfo(title="Complete", message=f"Well Done! You manage to learn new 100 french word's. "
                                                      f"Now you can just relearned the 100 word's")
        original_data = pandas.read_csv("data/french_words.csv")  # read csv file
        to_learn = original_data.to_dict(orient='records')  # convert dataFrame to list with
        # many dictionary's of french word with translation in english
    else:
        to_learn = data.to_dict(orient='records')  # convert dataFrame to list with
        # many dictionary's of french word with translation in english


# ---------------------------- WORD GENERATOR ------------------------------- #
"""when press on the known button (right_button) then the card will go to the next card"""


def next_card():
    global current_card_index, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) < 1:
        read_file()
    current_card_index = random.randint(0, len(to_learn) - 1)
    random_choice_card = to_learn[current_card_index]["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_choice_card, fill="black")
    canvas.itemconfig(card_background, image=front_img)

    flip_timer = window.after(3000, change_card)


# ---------------------------- FLIP THE CARD ------------------------------- #
"""when we wait 3 seconds or press on the cross button than th card will change to the translate card"""


def change_card():
    global current_card_index
    english_word = to_learn[current_card_index]["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")

    # To change the image:
    canvas.itemconfig(card_background, image=card_back_img)



# ---------------------------- WRITE TO FILE ------------------------------- #
"""if the card is known and the right button was pressed then the current word (french word)
   will be deleted from the word_to_learn file"""


def is_known():
    global to_learn
    global current_card_index
    to_learn.remove(to_learn[current_card_index])

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, change_card)

canvas = Canvas(height=526, width=800)
card_back_img = PhotoImage(file="./images/card_back.png")  # Back card image
front_img = PhotoImage(file="./images/card_front.png")  # front card image
card_background = canvas.create_image(400, 263, image=front_img)  # the main canvas that we going to flip every time
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=change_card)
unknown_button.grid(row=1, column=0)
right_mark_image = PhotoImage(file="./images/right.png")
Write_button = Button(image=right_mark_image, highlightthickness=0, command=is_known)
Write_button.grid(row=1, column=1)

next_card()

window.mainloop()
