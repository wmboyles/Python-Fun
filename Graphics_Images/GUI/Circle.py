from tkinter import *

canvas = Canvas(width=300, height=300, bg='white')  
canvas.pack(expand=YES, fill=BOTH)                

canvas.create_oval(10, 50, 200, 200, width=1, fill='red')

mainloop()
