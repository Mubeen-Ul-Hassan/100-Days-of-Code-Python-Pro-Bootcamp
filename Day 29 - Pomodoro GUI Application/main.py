import tkinter
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading_label.config(text="Timer")
    tick_icon_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        heading_label.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading_label.config(text="Break")
    else:
        count_down(work_sec)
        heading_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_icon_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg="white")

canvas = tkinter.Canvas(width=200, height=224, bg="white", highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 127, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(row=2, column=2)

heading_label = tkinter.Label(window, text="Timer", bg="white", font=("Arial", 30, "bold"))
heading_label.grid(row=1, column=2)

start_button = tkinter.Button(text="Start", highlightbackground="black", highlightcolor="black", highlightthickness=2, bg="white", width=6, font=("Arial", 15), command=start_timer)
start_button.grid(row=3, column=1)

reset_button = tkinter.Button(text="Reset", highlightbackground="black", highlightcolor="black", highlightthickness=2, bg="white", width=6, font=("Arial", 15), command=reset_timer)
reset_button.grid(row=3, column=3)

tick_icon_label = tkinter.Label(window, height=1, width=3, padx=5, pady=5, bg="white", fg="red", font=("Arial", 30, "bold"))
tick_icon_label.grid(row=4, column=2)

window.mainloop()