# Using a class to create a GUI with Tkinter

from tkinter import *  # Imports "Tkinter" graphics library


class Application(Frame):

    def __init__(self, master):  # Initalizes the frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):  # Will create 3 useless buttons
        self.button1 = Button(self, text="Button1 Text")  # Creates Button & text
        self.button1.grid()  # Grids Button

        self.button2 = Button(self)  # Creates button w/o text
        self.button2.grid()  # Grids button
        self.button2.configure(text="Button2 Text")  # creates button text

        self.button3 = Button(self)  # creates button w/o text
        self.button3.grid()  # grids button
        self.button3["text"] = "Button3 Text"  # Creates button text

        Button4String = "Button4 Text"  # Variable for button text
        self.button4 = Button(self, text=Button4String)  # Creates button
        self.button4.grid()  # grids button


root = Tk()  # creats window
root.title("OOP Buttons")  # names window
root.geometry("200x100")  # creates window size

app = Application(root)

root.mainloop()

