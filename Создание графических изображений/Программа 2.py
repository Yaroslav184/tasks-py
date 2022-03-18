from tkinter import *

def take():
    a['text'] = 'Выдано'

root = Tk()
Label(text='Пункт выдачи').pack()
Button(text='Взять', command=take).pack()
a = Label(width=10, height=1)
a.pack()
root.mainloop()