from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer_ = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer_)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

# If it's the 1st, 3rd, 5th, or 7th rep:
    if reps % 5 == 0:
        # If it's the 8th rep:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)

# if it's 2nd/4th/6th rep:
    elif reps % 3 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        timer.config(text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# window.after(1000, "Hello")


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_
        timer_ = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)


canvas = Canvas(width=210, height=230, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(105, 100, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", font=("Courier", 20), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)

window.mainloop()
