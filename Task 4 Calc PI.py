#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("1080x750")

def display_text1():
   global entry1 , entry2
   text= entry1.get()
   text= entry2.get()
   pi = int(entry1) / (2*int(entry2))
   label1.configure(int=pi)

#Initialize a Label to display the User Input
label1=Label(win, text="Enter the Random cicumference of circle :", font=("Courier 22 bold"))
label1.pack()


#Create First Entry widget to accept User Input
entry1= Entry(win, width= 70)
entry1.focus_set()
entry1.pack()

label2=Label(win, text="Enter the Random Radius of circle :", font=("Courier 22 bold"))
label2.pack()


#Create First Entry widget to accept User Input
entry2= Entry(win, width= 70)
entry2.focus_set()
entry2.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Start Execution",width= 40, command= display_text1).pack(pady=20)

win.mainloop()

