from tkinter import*
from tkinter import ttk

# Geometry Manager
# Pack - defines how widgets are located
# Typical locations - Top, Right, Bottom, Left
# Stretch Componets - X, Y, Both, None

root = Tk()

frame = Frame(root)

Label(frame, text="Buttons!").pack()

# Button named B1 on the left-most side filled with the Y coordinate
Button(frame, text="B1").pack(side=LEFT, fill=Y)

Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()