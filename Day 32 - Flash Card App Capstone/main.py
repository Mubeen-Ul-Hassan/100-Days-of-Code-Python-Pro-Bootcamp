import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
import random
import os

# ----------------------------------
BACKGROUND_COLOR = "#B1DDC6"
click = 1
current_car_content = {}

def next_card():
    global current_card_content, click
    df = pd.read_csv("./data/german_words.csv")
    data_dict = df.to_dict(orient="records")

    current_card_content = random.choice(data_dict)

    current_language = "German"
    current_language_word = current_card_content[current_language]

    change_img_and_content(current_language, current_language_word, "front")

    current_card_content.update({"English": current_card_content["English"]}) 
    print(f"German: {current_card_content['German']}, English: {current_card_content['English']}")

    current_language = "English"
    current_language_word = current_card_content[current_language]

    window.after(3000, change_img_and_content, current_language, current_language_word, "back")
    


def change_img_and_content(lang, word, card_side):
    
    card_img = card_front_img
    color = "black"
    if card_side == "back": 
        card_img = card_back_img
        color = "white"

    image_container = canvas.create_image(400, 263, image=card_img)
    canvas.itemconfig(image_container, image=card_img)
    canvas.create_text(400, 150, text=lang, font=("Ariel", 40, "italic"), fill=color)
    canvas.create_text(400, 263, text=word, font=("Ariel", 50, "bold"), fill=color)

    canvas.image = card_img


def tick():
    global current_card_content


    df = pd.read_csv("./data/german_words.csv")
    df = df[df["German"] != current_card_content["German"]]
    df.to_csv("./data/german_words.csv", index=False)

    file_exists = os.path.isfile("./data/german_words.csv")
    new_record = pd.DataFrame([current_card_content])
    new_record.to_csv("./data/words_to_learn.csv", mode="a", index=False, header=not file_exists)
    next_card()
    return True

def wrong():
    global current_card_content
    current_card_content.clear()
    next_card()
    return False

# ----------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Germany", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, width=350, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, borderwidth=0, highlightthickness=0, command=wrong)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, borderwidth=0, highlightthickness=0, command=tick)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()