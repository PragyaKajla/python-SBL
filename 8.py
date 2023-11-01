# design a GUI using Tkinter for a given application
# 1. simiple Start button
# 2. entry field for - login and password

# start button
import tkinter as tk
r = tk.Tk()
r.title('login')
button = tk.Button(r, text = 'Start', width = 25, command = r.destroy)
button.pack()
r.mainloop()

#entry fields
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
