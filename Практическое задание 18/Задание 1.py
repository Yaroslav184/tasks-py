from tkinter import*

root = Tk()
root.title('Регистратор символов')
text = Text(root, width=50, height=30, highlightthickness=6)

def reportEvent(event):
    print('keysym=%s, keysym_num=%s' % (event.keysym, event.keysym_num))

text.bind('<KeyPress>', reportEvent)
text.pack(expand=1, fill='both')
text.focus_set()
root.mainloop()
