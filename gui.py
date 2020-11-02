#Number System Tools
#Sunday, November 1, 2020

from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style()
style.configure("T.TFrame", borderwidth = 10, relief = "sunken")

content = ttk.Frame(root).grid()
numbers = ttk.Frame(content).grid(row = 1, column = 0)
#options = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100).grid(row = 1, column = 1)

decimalFrame = ttk.Frame(numbers, style="T.TFrame", padding = (3, 3, 12, 12)).grid(row = 0, column = 0)
decimalLabel = ttk.Label(decimalFrame, text = "Decimal").grid(row = 0, column = 0)
decimalEntry = ttk.Entry(decimalFrame, textvariable="decimal").grid(row = 1, column = 0)

#hexadecimalEntry = ttk.Entry(numbers, textvariable="hexadecimal").grid(row = 1, column = 0)

#binaryEntry = ttk.Entry(numbers, textvariable="Binary").grid(row = 2, column = 0)

root.mainloop()