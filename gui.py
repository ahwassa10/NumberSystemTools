#Number System Tools
#Sunday, November 1, 2020

from tkinter import *
from tkinter import ttk

root = Tk()
root.tk.call('tk', 'scaling', 1.0)

style = ttk.Style()
style.configure("TButton", foreground="green", padding=(3, 3, 12, 12), font=("Consolas", 12))
style.configure("TFrame", background="black")

content = ttk.Frame(root, padding = (10, 10, 10, 10)).grid(row=0, column=0)
styledButton = ttk.Button(content, text="Style Testing").grid(row=0, column=0)
styledEntry = ttk.Entry(content).grid(row=1, column = 0, sticky="WE")
textb = Text(content).grid(row=2, column=0, sticky="WE")


root.mainloop()