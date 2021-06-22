from tkinter import *


def enter(event):
    line = str(eval(e1.get()))
    e1.delete(0, END)
    e1.insert(0, line)


def dell(event):
    e1.delete(0, END)


def dot(event):
    e1.insert(len(e1.get()), ".")


def amount(event):
    e1.insert(len(e1.get()), "+")


def difference(event):
    e1.insert(len(e1.get()), "-")


def multiply(event):
    e1.insert(len(e1.get()), "*")


def division(event):
    e1.insert(len(e1.get()), "/")


def zero(event):
    e1.insert(len(e1.get()), "0")


def one(event):
    e1.insert(len(e1.get()), "1")


def two(event):
    e1.insert(len(e1.get()), "2")


def three(event):
    e1.insert(len(e1.get()), "3")


def four(event):
    e1.insert(len(e1.get()), "4")


def five(event):
    e1.insert(len(e1.get()), "5")


def six(event):
    e1.insert(len(e1.get()), "6")


def seven(event):
    e1.insert(len(e1.get()), "7")


def eight(event):
    e1.insert(len(e1.get()), "8")


def nine(event):
    e1.insert(len(e1.get()), "9")


root = Tk()
root.title("Калькулятор 3.0")
root.geometry('400x450')

f_e1 = Frame(root)
fEnter = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

e1 = Entry(f_e1, width=30)

Division = Button(f1, text="/", width=5, height=3)
Multiply = Button(f1, text="*", width=5, height=3)
Difference = Button(f1, text="-", width=5, height=3)
Amount = Button(f5, text="+", width=5, height=3)
Enter = Button(fEnter, text="=", width=5, height=3)
Delete = Button(fEnter, text="C", width=5, height=3)

b0 = Button(f5, text="0", width=5, height=3)
b1 = Button(f4, text="1", width=5, height=3)
b2 = Button(f4, text="2", width=5, height=3)
b3 = Button(f4, text="3", width=5, height=3)
b4 = Button(f3, text="4", width=5, height=3)
b5 = Button(f3, text="5", width=5, height=3)
b6 = Button(f3, text="6", width=5, height=3)
b7 = Button(f2, text="7", width=5, height=3)
b8 = Button(f2, text="8", width=5, height=3)
b9 = Button(f2, text="9", width=5, height=3)

bDot = Button(f5, text=".", width=5, height=3)

f_e1.pack()
fEnter.pack()
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()

e1.pack(side=LEFT, pady=5)
Delete.pack(side=LEFT, padx=15, pady=5)
Enter.pack(side=LEFT, padx=15, pady=5)

Division.pack(side=LEFT, padx=15, pady=5)
Multiply.pack(side=LEFT, padx=15, pady=5)
Difference.pack(side=LEFT, padx=15, pady=5)

b1.pack(side=LEFT, padx=15, pady=5)
b2.pack(side=LEFT, padx=15, pady=5)
b3.pack(side=LEFT, padx=15, pady=5)
b4.pack(side=LEFT, padx=15, pady=5)
b5.pack(side=LEFT, padx=15, pady=5)
b6.pack(side=LEFT, padx=15, pady=5)
b7.pack(side=LEFT, padx=15, pady=5)
b8.pack(side=LEFT, padx=15, pady=5)
b9.pack(side=LEFT, padx=15, pady=5)

Amount.pack(side=LEFT, padx=15, pady=5)
b0.pack(side=LEFT, padx=15, pady=5)
bDot.pack(side=LEFT, padx=15, pady=5)

Amount.bind("<Button-1>", amount)
Difference.bind("<Button-1>", difference)
Multiply.bind("<Button-1>", multiply)
Division.bind("<Button-1>", division)

b0.bind("<Button-1>", zero)
b1.bind("<Button-1>", one)
b2.bind("<Button-1>", two)
b3.bind("<Button-1>", three)
b4.bind("<Button-1>", four)
b5.bind("<Button-1>", five)
b6.bind("<Button-1>", six)
b7.bind("<Button-1>", seven)
b8.bind("<Button-1>", eight)
b9.bind("<Button-1>", nine)
bDot.bind("<Button-1>", dot)

Enter.bind("<Button-1>", enter)
Delete.bind("<Button-1>", dell)
e1.bind("<Return>", enter)
root.mainloop()
