# Python Graphics: Binding Buttons

from tkinter import *  # Imports "Tkinter" graphics library


class Application(Frame):  # creats GUI application

    def __init__(self, master):  # Initalizes the frame
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0  # counts button clicks
        self.create_widgets()

    def create_widgets(self):  # Will create button that displays click number
        self.button = Button(self)  # Creates Button & text
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count  # references next def
        self.button.grid()  # Grids Button

    def update_count(self):  # event handler
        self.button_clicks += 1  # increases click count
        self.button["text"] = "Total Clicks: " + str(self.button_clicks)  # display total

        
root = Tk()  # creates window
root.title("Counting Buttons")  # names window
root.geometry("300x100")  # creates window size

app = Application(root)

root.mainloop()
