from tkinter import *

root = Tk()
root.title('Калькулятор')

frame_xy = Frame(root)
frame_xy.pack(side=TOP, expand=YES, fill=X)

labelx = Label(frame_xy, text='x = ')
labelx.pack()

entryX = Entry(frame_xy)
entryX.insert(0, 0)
entryX.focus()
entryX.pack()

labely = Label(frame_xy, text='y = ')
labely.pack()

entryY = Entry(frame_xy)
entryY.insert(0, 0)
entryY.focus()
entryY.pack()

frame_op = LabelFrame(root, text="Операция:")
frame_op.pack()

oper = ['+', '-', '*', '/']

varOper = StringVar()

for op in oper:
    Radiobutton(frame_op, text=op, variable=varOper, value=op).pack(side=LEFT, padx=20, pady=10)

varOper.set(oper[0])

frame_res = Frame(root)
frame_res.pack()

label_ans = Label(frame_res, text='Ответ: ')
label_ans.pack(side=RIGHT, padx=10, pady=10)

def Calc():
    x = float(entryX.get())
    y = float(entryY.get())

    op = varOper.get()
    answer_list = {
        '+': x + y,
        '-': x - y,
        '/': x / y,
        '*': x * y
    }
    ans = answer_list[op]

    label_ans.config(text='Ответ: ' + str(ans))

button_result = Button(frame_res, text="=", width=10, command=Calc)
button_result.pack(side=LEFT, padx=30, pady=20)

root.mainloop()
