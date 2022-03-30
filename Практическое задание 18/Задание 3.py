# Задание №1
# Ильин Ярослав 1993
# Вариант 6

from tkinter import *

prog = Tk()
prog.title('Цвета')

Label(master=prog, width=7, height=4, bg='light blue', text="4").pack(anchor=S)
Label(master=prog, width=7, height=4, bg='light green', text="3").pack(anchor=S)
Label(master=prog, width=7, height=4, bg='orange', text="2").pack(anchor=S)
Label(master=prog, width=7, height=4, bg='yellow', text="1").pack(anchor=S)

prog.mainloop()