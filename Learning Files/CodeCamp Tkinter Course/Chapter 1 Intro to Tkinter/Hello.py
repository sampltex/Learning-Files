from tkinter import *
# in tkinter everything is a widget
# the first thing you make is a root widget/window
# there are two steps, first define the thing and then put it on the screen

root = Tk() # this is the root widget and always need to happen first
# its like the int main() function that defines the start of a program in c++

myLabel = Label(root, text="Hello World!") # this is a widget. The first argument is where it goes (so the root widget)

myLabel.pack() # this is the "unsophisticated method" of putting things on the screen

root.mainloop() # you also need to loop the program so it can figure out what is happening