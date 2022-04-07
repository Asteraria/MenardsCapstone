# GUI Environment Program
# Written Nathan Meeker
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, askokcancel

# create the root window
root = tk.Tk()
root.title('Select Config File')
root.resizable(False, False)
root.geometry('300x150')
filename = "null"
greeting = tk.Label(text="Menards Router/Switch Deployment")

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    #formatting of file selection dialog box
    global filename #stores the filename globally so it can be called on outside of the function
    filename = fd.askopenfilename(
        title='Select a configuration file',
        initialdir='C:', #Change this path to the desired starting folder
        filetypes=filetypes)

    #Confirmation window that displays path
    answer = askokcancel("Confirm", message=filename)
    if answer: #If the user select OK, the windows will close, if they select Cancel, they can select a different file.
        #print(filename)
        close() #calls the close function
    

#function to close the windows after file selection
def close():
    root.destroy()
    
# open button
open_button = ttk.Button(
    root,
    text='Select a file',
    command=select_file
)
greeting.pack()
open_button.pack(expand=True)

# run the application
root.mainloop()