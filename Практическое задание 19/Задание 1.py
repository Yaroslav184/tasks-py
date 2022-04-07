from tkinter import *

root = Tk()
root.title('Текст')

label_1 = Label(root, text='Подтвердите или опровергните утверждение: ', font=('Helvetica', 14))
label_2 = Label(root, text='Язык Python ялвляется объектно-ориентированным?')
label_3 = Label(root, text='(поставьте галочку, если утверждение верно)')

var = IntVar()
var.set(1)

def cheak():
    if var.get() == 1:
        master = Tk()
        message = Message(master, text='ПОЗДРАВЛЯЮ!Вы ответили правильно!', width=300)
        message.pack()
        master.mainloop()
    else:
        master = Tk()
        message = Message(master, text='ПЛОХО! Вы ответили неверно!', width=300)
        message.pack()
        master.mainloop()

cheak_box = Checkbutton(root, text='Да/Нет', variable=var)
button = Button(root, text='Проверить', command=cheak)

label_1.grid(row=0, column=0, sticky=W)
label_2.grid(row=1, column=0, sticky=W)
label_3.grid(row=3, column=0, sticky=W)

cheak_box.grid(row=2, column=0, sticky=W)
button.grid(row=4, column=0, sticky=W)

root.mainloop()
