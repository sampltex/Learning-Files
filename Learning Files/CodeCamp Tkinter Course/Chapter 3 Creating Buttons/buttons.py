from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="red") 
# bg makes the background a color (string) takes names of colors and hex codes
# fg makes the text a color (string) takes names of colors and hex codes
# tell it to do something with command=(function) dont put in arguments
# make a button bigger with padx= and pady= and disabled a button with state=DISABLED
# the first thing you specify in widgets is always where it goes aka the root
myButton.pack() # you also need to put buttons on the screen



root.mainloop()