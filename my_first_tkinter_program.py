from tkinter import *

root = Tk()

root.title("Welcome to GeekForGeeks")
root.geometry('600x450')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label(root, text="Are you a Geek?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)


def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text="I just got clicked")


btn = Button(root, text="Click me",
             fg="red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()

