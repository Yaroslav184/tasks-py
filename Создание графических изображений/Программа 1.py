from tkinter import *

root = Tk()
e1 = Entry(width=50)

def insert():
    e1.insert(0, 'Hello World! ')
b = Button(text='Вставить', command=insert)
e1.pack()
b.pack()
root.mainloop()