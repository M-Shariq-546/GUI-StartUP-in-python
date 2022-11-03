# Python program to create a close button
from tkinter import *

# Creating the tkinter window with tk name
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Click to Exit", command=root.destroy)
exit_button.pack(pady=20)

root.mainloop()
