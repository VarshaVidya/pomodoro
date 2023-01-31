from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00", fill="white")
    check_mark.config(text="")
    global reps
    reps =0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%8==0:
        countdown_mech(long_break_sec)
        title.config(text="Break",fg= RED)
    elif reps%2==0:
        countdown_mech(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        countdown_mech(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown_mech(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    if count > 0:
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000,countdown_mech,count-1)
    else:
        start_countdown()
        tick_mark =""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            tick_mark +="✔"
        check_mark.config(text=tick_mark)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title('pomodoro')

window.config(padx=100,pady=50,bg = YELLOW)

title = Label(text="Timer",fg= GREEN,bg = YELLOW,font =(FONT_NAME,50,"bold"))
title.grid(column = 1,row = 0)

canvas = Canvas(width = 200, height= 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file ="tomato.png")
tomato = canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font =("Courier",35,"bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text="Start",command = start_countdown)
start_button.grid(column = 0,row = 2)

reset_button = Button(text="Reset",command = reset_timer)
reset_button.grid(column = 2,row = 2)

check_mark = Label(fg= GREEN,bg = YELLOW)
check_mark.grid(column=1,row = 3)

window.mainloop()