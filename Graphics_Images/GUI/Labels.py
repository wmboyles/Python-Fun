# Python Graphics: Labels

from tkinter import *  # Imports graphics library
root = Tk()  # Creates window

root.title("Labels")  # Titles window
root.geometry("200x100")  # Specifies window size

app = Frame(root)  # Creates "frame"
app.grid()  # Grids "frame"
label = Label(app, text="This is a label. It is GUI text.")  # Creats label
label.grid()  # grids label

root.mainloop()  # runs window
