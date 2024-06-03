from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
# make a border with borderwidth=
# you can also use fg and bg like buttons (chapter 3)
# use width= to make it wider
# to make an input you use Entry()
e.pack()
e.insert(0, "Enter Your Name") # inserts a default text into the Entry
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello) # .get() method allows the label to "read" the Entry given
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick) 

myButton.pack() 



root.mainloop()