from tkinter import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.count = 0
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self)
        self.button["text"] = "Total Clicks: "
        self.button["command"] = self.update_count
        self.button.grid()

    def update_count(self):
        self.count += 1
        self.button["text"] = "Total Clicks: " + str(self.count)


root = Tk()
root.title("Counter")
root.geometry("500x500")

app = Application(root)
root.mainloop()
