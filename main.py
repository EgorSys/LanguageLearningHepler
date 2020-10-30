from tkinter import *
from Program import *

if __name__ == '__main__':
    root = Tk()
    root.geometry('520x400+350+200')

    program = Program(root)
    program.pack()

    root.mainloop()