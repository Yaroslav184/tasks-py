from tkinter import *

root = Tk()
root.title('Координаты мыши')

def mouse_move(event):
    print(event.x, event.y)

root.bind('<Motion>', mouse_move)

root.mainloop()
