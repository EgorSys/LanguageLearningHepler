from tkinter import *
from Program import *

if __name__ == '__main__':
    root = Tk()
    root.geometry('520x400+350+200')
    root.title("Language Learning Helper")

    frame = Frame(root)
    program = Program(frame)
    program.pack()

    root.mainloop()