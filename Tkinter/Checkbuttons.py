from tkinter import *


def Left(event):
    chk = [chk1.get(), chk2.get(), chk3.get(), chk4.get(), chk5.get()]
    if len(txt.get()) > 0:
        txt.delete(0, END)
    for i in range(5):
        if chk[i] == 1:
            txt.insert(len(txt.get()), str(i + 1))


def Right(event):
    chk = [chk1.get(), chk2.get(), chk3.get(), chk4.get(), chk5.get()]
    if len(txt.get()) > 0:
        txt.delete(0, END)
    for i in range(5):
        if chk[i] == 0:
            txt.insert(len(txt.get()), str(i + 1))


root = Tk()
root.title("Флажки")
root.geometry("400x300")

txt = Entry(root, width=30)
txt.pack()

chk1 = IntVar()
chk1.set(0)
c1 = Checkbutton(text='1', variable=chk1, onvalue=1, offvalue=0)
c1.pack()

chk2 = IntVar()
chk2.set(0)
c2 = Checkbutton(text='2', variable=chk2, onvalue=1, offvalue=0)
c2.pack()

chk3 = IntVar()
chk3.set(0)
c3 = Checkbutton(text='3', variable=chk3, onvalue=1, offvalue=0)
c3.pack()

chk4 = IntVar()
chk4.set(0)
c4 = Checkbutton(text='4', variable=chk4, onvalue=1, offvalue=0)
c4.pack()

chk5 = IntVar()
chk5.set(0)
c5 = Checkbutton(text='5', variable=chk5, onvalue=1, offvalue=0)
c5.pack()

txt.bind("<Button-1>", Left)
txt.bind("<Button-3>", Right)

root.mainloop()
