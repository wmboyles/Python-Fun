# Python Graphics: Buttons

from tkinter import *  # Import Graphics Library

root = Tk()  # Create Window

root.title("Buttons")  # Name Window
root.geometry("200x100")  # Give window size

app = Frame(root)  # Creates "frame"
app.grid()  # Inserts "app" into grid/display

button1 = Button(app, text="Button1 Text")  # Creates Button & Text
button1.grid()  # Grids Button

button2 = Button(app)  # Creates Button w/o text
button2.grid()  # Grids Button
button2.configure(text="Button2 Text")  # Creates button text

button3 = Button(app)  # Creates button w/o text
button3.grid()  # Grids button
button3["text"] = "Button3 Text"  # Creates button text

ButtonString = "Button4 Text"  # Creats string for button text
button4 = Button(app, text=ButtonString)  # creates button & passes in string
button4.grid()  # grids button

root.mainloop()  # Run window
