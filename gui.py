#Number System Tools
#Sunday, November 1, 2020

from tkinter import *
from tkinter import ttk

root = Tk()
content = ttk.Frame(root).grid()

decimalEntry = ttk.Entry(content, textvariable="decimal").grid(row = 0, column = 0)

hexadecimalEntry = ttk.Entry(content, textvariable="hexadecimal").grid(row = 1, column = 0)

binaryEntry = ttk.Entry(content, textvariable="Binary").grid(row = 2, column = 0)