from tkinter import *

root = Tk()
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name is John Doe").grid(row=1, column=4)

# you can make a grid by using the .grid() method
# you can also use the method as you declare the label
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=4)

root.mainloop()