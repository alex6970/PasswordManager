from tkinter import * # (python GUI)
from tkinter import ttk

root = Tk()
root['bg'] = 'white'
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.quit).grid(column=1, row=0)
root.mainloop()
