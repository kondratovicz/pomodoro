import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50)
canvas = tkinter.Canvas(width=200, height= 224)
pomodoro_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=pomodoro_image)
canvas.create_text(text="allo")
canvas.pack()



window.mainloop()