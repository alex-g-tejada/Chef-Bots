#import tkinter
from tkinter import*
from tkinter import ttk

# tkinter._test() Default test for tkinter

# Tk object - root will be the main window
root = Tk()

# Window Title
root.title("First GUI")

# TK Button with title
#ttk.Button(root, text="Hello World").grid()

# TK Frame - Used to Surround other widgets
frame = Frame(root)

labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

labelText.set("I am a label")

# Reposition the widgets
label.pack()
button.pack()
frame.pack()

# Allow the main window to be visible
root.mainloop()

