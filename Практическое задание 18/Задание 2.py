# Задание №1
# Ильин Ярослав 1993

from tkinter import *

prog = Tk()
prog.title('Кнопка')

def change(event):
    b['fg'] = 'red'
    b['activeforeground'] = 'yellow'

b = Button(master=prog, text='red', width=10, height=3)
b.bind('<Button>-1', change)
b.bind('<Return>', change)
b.focus_set
b.pack(anchor=S)

prog.mainloop()