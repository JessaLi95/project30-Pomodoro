from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break)
        label1.config(text="Long break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)
    else:
        count_down(short_break)
        label1.config(text="Short break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✓️"
        label2.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


label1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
label1.grid(column=2, row=1)
label2 = Label(bg=YELLOW, fg=GREEN)
label2.grid(column=2, row=4)

button1 = Button(text="Start", command=start_timer, highlightthickness=0)
button2 = Button(text="Reset", command=reset_timer, highlightthickness=0)
button1.grid(column=1, row=3)
button2.grid(column=3, row=3)

window.mainloop()