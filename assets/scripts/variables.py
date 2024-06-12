import tkinter as tk

with open('assets/data/winfo.txt') as f:
    string = f.read().splitlines()

width = int(string[0])
height = int(string[1])

root = tk.Tk()

x = int((root.winfo_screenwidth() / 2) - (width / 2))
y = int(((root.winfo_screenheight() - 120) / 2) - (height / 2))