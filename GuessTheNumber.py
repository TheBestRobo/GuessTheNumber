from tkinter import *

import random
import os, sys

screen = Tk()

screen.title("Guess the number")
screen.configure(background="#16697A")
screen.resizable(height=False, width=False)

t = 0

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def chck(event):
    global a
    global t
    n = int(ent.get())
    if n > a:
        t += 1
        img.configure(image=down)
        tr.configure(text="Tries: " + str(t))
        ent.delete(0, END)
    elif n < a:
        t += 1
        img.configure(image=up)
        tr.configure(text="Tries: " + str(t))
        ent.delete(0, END)
    elif n == a:
        t += 1
        img.configure(image=correct)
        t = 0
        ent.delete(0, END)
    if t == 0:
        tr.configure(foreground="white")
    if t > 0:
        tr.configure(foreground = "green")
    if t > 4:
        tr.configure(foreground="yellow")
    if t > 10:
        tr.configure(foreground="red")



def ext():
    screen.destroy()

def numb():
    global a
    global choice
    df = choice.get()
    tr.configure(text="Tries: ")
    if df == 1:
        a = random.randint(0, 50)
        print(a)
    elif df == 2:
        a = random.randint(0, 100)
        print(a)
    else:
        a = random.randint(0, 200)
        print(a)
    ent.configure(state="normal")
    img.configure(image=dice)


lbl1 = Label(screen, text = "Guess The Number", foreground = "#EDE7E3", background = "#16697A", font = ('Comic Sans MS', 16))
lbl1.grid(row=0, column=0, columnspan = 3)

choice = IntVar()
choice.set(2)

up = PhotoImage(file= resource_path("uparrow.png"))
down = PhotoImage(file= resource_path("downarrow.png"))
correct = PhotoImage(file=resource_path("correct.png"))
dice = PhotoImage(file=resource_path("dice.png"))

ea = Radiobutton(screen, text = "Easy: 0-50",background="#16697A", foreground="white", font = ('Comic Sans MS', 14),value = 1, variable = choice)
md = Radiobutton(screen, text = "Medium: 0-100", background="#16697A", foreground="white", font = ('Comic Sans MS', 14), value = 2, variable = choice)
hd = Radiobutton(screen, text = "Hard: 0-200", background="#16697A", foreground="white", font = ('Comic Sans MS', 14), value = 3, variable = choice)
ea.grid(row=1, column=0)
md.grid(row=1, column=1)
hd.grid(row=1, column=2)

lbl2 = Label(screen, text = "In this game you will try to find a secret number that", foreground = "#EDE7E3", background = "#16697A", font = ('Comic Sans MS', 14))
lbl2.grid(row=2, column=0, columnspan = 3)

lbl3 = Label(screen, text = " is redomly chosen every round. Try to guess it with ", foreground = "#EDE7E3", background = "#16697A", font = ('Comic Sans MS', 14))
lbl3.grid(row=3, column=0, columnspan = 3)

lbl4 = Label(screen, text = " the least tries possible.", foreground = "#EDE7E3", background = "#16697A", font = ('Comic Sans MS', 14))
lbl4.grid(row=4, column=0, columnspan = 3)

ent = Entry(screen, state="disabled")
ent.grid(row=5, column=1)

img = Label(screen, image=dice, background = "#16697A")
img.grid(row=5, column=0)

ran = Button(screen, text = "Randomize", background="#16697A", foreground="white", command=numb)
ran.grid(row=5, column=2)

tr = Label(screen, text = "Tries: ",background="#16697A", foreground="white")
tr.grid(row=6, column=1)

ex = Button(screen, text = "Exit", background="#16697A", foreground="white",command=ext)
ex.grid(row=6, column=2)


screen.bind("<Return>", chck)

screen.mainloop()

#Ok, works...