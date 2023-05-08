import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#FF6969"
GREEN = "#245953"
BLUE = "#A6D0DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 == 1 or reps == 0:
        timer_label.config(text="Work!", fg=RED)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Rest!", fg=GREEN)
        count_down(long_break)
    else:
        timer_label.config(text="Rest!", fg=GREEN)
        count_down(short_break)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
            check_marks.config(text=mark, fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50, bg=BLUE)

timer_label = tkinter.Label(text="Timer", background=BLUE, font=(FONT_NAME, 35, "bold"), fg="white")
timer_label.grid(row=0, column=1)
canvas = tkinter.Canvas(width=200, height= 224, bg=BLUE, highlightthickness=0)
pomodoro_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_image)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
check_marks = tkinter.Label(bg=BLUE)
check_marks.grid(row=3, column=1)

window.mainloop()