import tkinter
from tkinter import *
import random
from tkinter import messagebox

answer = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

word = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num =  random.randrange(0, len(word), 1)

def default():
    global word,answer,num
    lbl.config(text = word[num])

def res():
    global word,answer,num
    num = random.randrange(0, len(word), 1)
    lbl.config(text = word[num])
    e1.delete(0, END)


def checkans():
    global word,answer,num
    var = e1.get()
    if var == answer[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)




main_window = tkinter.Tk()
main_window.geometry("350x400+400+300")
main_window.title("Jumbbled")
main_window.configure(background = "#000000")

lbl = Label(
    main_window,
    text = "Your here",
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
    main_window,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    main_window,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    main_window,
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

default()
main_window.mainloop()
