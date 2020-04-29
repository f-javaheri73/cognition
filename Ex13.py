import tkinter as tk
win = tk.Tk()
password = '12345'
user = 'admin'

def func():
    if en1.get() == user and en2.get() == password:
        btn1.config(background = 'green')
    else:
        btn1.config(background = 'red')
        
lb1 = tk.Label(win, text = 'user name')
en1 = tk.Entry(win)
lb2 = tk.Label(win, text = 'password')
en2 = tk.Entry(win)
btn1 = tk.Button(win, text = 'log in',command = func)

lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
btn1.pack()

win.mainloop()
