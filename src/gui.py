import tkinter as tk
from tkinter import ttk

global keywordTyped

win = tk.Tk()
win.title("Job Search by JLXW")


aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def buttonClicked():
    keywordTyped = str.get()
    print(keywordTyped)

ttk.Label(win, text="Enter a keyword").grid(column=0, row=0)

str= tk.StringVar()
strTyped = ttk.Entry(win, width=12, textvariable=str)
strTyped.grid(column=0, row=1)

button = ttk.Button(win, text="Search", command=buttonClicked)
button.grid(column=1, row=1)
win.mainloop()