import tkinter as tk

win = tk.Tk()
lb1 = tk.Label(win, text = 'user name')
en1 = tk.Entry(win)
lb2 = tk.Label(win, text = 'password')
en2 = tk.Entry(win)
btn1 = tk.Button(win, text = 'log in')

lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
btn1.pack()
 
