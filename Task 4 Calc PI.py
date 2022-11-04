#Import the required Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import docx

#Creating Document ready
doc = docx.Document()


#Creating a Heading
doc.add_Heading('Pi Calculator' ,1)


doc.save('file.docx')

#from PIL import Image

#myimg = Image.open('pic.jpg')
#myimg.size('500x300')
#myimg.show()


# FG Color
fgColor = '#1e81b0'

#Create an instance of Tkinter frame
win= Tk()
win.title("PI Calculator by random values By M. Shariq Shafiq")

# Changing the background
win.configure(bg='white')

#Set the geometry of Tkinter frame
win.geometry("900x550")

frame = Frame(win , bg = 'white')
frame.pack(fill = 'both')

#Initialize a Label to display the User Input
label1=Label(frame, text="Enter the Random Circumference of Circle :", font=("Courier 15 bold"))
label1.configure(bg='white',fg=fgColor)
label1.grid(row = 0 , column = 0)

#Create First Entry widget to accept User Input
entry1= ttk.Entry(frame,font=("Courier 15 bold"))
entry1.grid(row = 0 , column = 1 , sticky='we' , padx=[0,40])

label2=Label(frame, text="Enter the Random Radius of Circle :", font=("Courier 15 bold"))
label2.configure(bg='white',fg=fgColor)
label2.grid(row = 1 , column = 0)

#Create First Entry widget to accept User Input
entry2= ttk.Entry(frame,font=("Courier 15 bold"))
entry2.grid(row = 1 , column = 1 , sticky='we' ,padx= [0,40])

label3=Label(win, text="", font=("Courier 15 bold"))
label3.configure(bg='white',fg='red')
label3.pack()
frame.rowconfigure((0,1,2) , weight = 1)
frame.columnconfigure((0,1) , weight = 1)

def display_text1(event=None):
   if entry1.get() == "":
      messagebox.showinfo(title="Value Missing", message="Enter Value of Circumference of Circle!")
   if entry2.get() =="":
      messagebox.showinfo(title="Value Missing", message="Enter Value of Radius!")
      entry2.focus_set()
   else:
      try:
         value1 = float(entry1.get())
         value2 = float(entry2.get())
      except:
         messagebox.showerror(title="Error",message="Please Enter Numeric or float data in fields!")
         entry1.delete(0, END)
         entry2.delete(0, END)
         entry1.focus_set()
      else:
         pi = (value1) / (2*value2)
         label3.configure(text=f"Value of PI = {pi}")

#Create a Button to validate Entry Widget
submit = Button(win, text= "Start Execution", command= display_text1)
submit.configure(bg=fgColor,fg='white' , font=("Courier 15 bold"))
submit.pack(pady=20)
# Setting focus to the first most entry
entry1.focus_set()

# Binding enter button for output
win.bind("<Return>",display_text1)

#infinite loop for gui
win.mainloop()

