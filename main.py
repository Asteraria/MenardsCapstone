# Main program to run modules
# Written by Grant Bruehl 4/5/22
from tkinter import mainloop
import load_replace
import GUI

def main():
    filename = GUI.filename

    GUI.root.mainloop()
    load_replace.main(filename)

if __name__ == "__main__":
    main()