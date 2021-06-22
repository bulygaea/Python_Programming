from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter import messagebox


def _open():
    txt.delete(1.0, END)
    op = askopenfilename()
    for l in fileinput.input(op):
        txt.insert(END, l)


def _save():
    try:
        file_name = asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        f.write(txt.get(1.0, END))
        f.close()
        return 0
    except FileNotFoundError:
        return -1


def _exit():
    answer = messagebox.askyesno("Подтверждение", "Сохранить и выйти?")
    if answer:
        error = _save()
        if error == -1:
            return
    root.destroy()


root = Tk()

m = Menu(root, tearoff=0)
root.config(menu=m)

fm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open...", command=_open)
fm.add_command(label="Save...", command=_save)
fm.add_command(label="Exit", command=_exit)

txt = Text(root, width=40, height=15, font="12")
txt.pack()

root.mainloop()
