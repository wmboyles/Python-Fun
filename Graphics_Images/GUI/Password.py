from tkinter import * #Imports "Tkinter" graphics library

class Application(Frame): #creats GUI application
    def __init__(self, master): #Initalizes the frame
        Frame.__init__(self,master)
        self.grid() #grids frame
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "Enter the Password")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.instruction = Label(self, text = "              Password: ")
        self.instruction.grid(row = 1, column =0, columnspan = 2, sticky = W)
        
        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, stick = W)
        
        self.submitbutton = Button(self, text = "Submit", command = self.reveal)
        self.submitbutton.grid(row = 2, column = 0, sticky = W)
        
        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        content = self.password.get()
        if content == "password":
            message = "Correct"
        else:
            message = "Incorrect"
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)


root = Tk() #creates window
root.title("Password") #names window
root.geometry("250x150") #creates window size

app = Application(root)

root.mainloop()
