# Nampalm Load Config Script
# Written by Grant Bruehl 3/31/22
from __future__ import print_function

import napalm
import sys
import os

#Nathan added for Tkinter Status GUI 4/9/22
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, askokcancel


#Nathan's added status box

# create the master status window
master = tk.Tk()
master.title('Configuration Status')
master.resizable(False, False)
master.geometry('300x500')


def opening_status():  
        myLabel = Label(master, text="Opening...")
        myLabel.pack() 
        
def loading_status():
        myLabel2 = Label(master, text="Loading replacement candidate...") 
        myLabel2.pack()

def differences_status():
        myLabel3 = Label(master, text="Finding differences:") 
        myLabel3.pack()
        #myLabel4 = Label(master, text=device.compare_config()) # Hopefully this isn't needed if it works in the block below
        #myLabel4.pack()

def committing_status():  
        myLabel5 = Label(master, text="Committing...")
        myLabel5.pack() 

def discarding_status():  
        myLabel6 = Label(master, text="Discarding...")
        myLabel6.pack() 

def done_status():  
        myLabel7 = Label(master, text="Device Session Closed")
        myLabel7.pack() 

def path_status():  
        myLabel8 = Label(master, text='Please supply the full path to "new_good.conf"')
        myLabel8.pack() 



def main(config_file):

    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg)

    print("Loading config file {0}.".format(config_file))

    # Use the appropriate network driver to connect to device:
    driver = napalm.get_network_driver("ios")

    # Connect:
    device = driver(
        hostname="10.10.10.10", #REPLACE WITH CONSOLE SERVER IP
        username="cisco", #REPLACE WITH SECURE METHOD
        password="cisco", #REPLACE WITH SECURE METHOD
        optional_args= {'secret': "cisco"}
        #optional_args={'secret':"cisco", "port":2001} #TO BE USED WITH CONSOLE SERVER PORTS 
    )

    opening_status()
    device.open()

    loading_status()
    device.load_replace_candidate(filename=config_file)

    # Note: Config has not been applied at this point
    # Prompt user to commit or discard changes:
    differences_status()

    answer2 = askokcancel("Confirm Differences", message=device.compare_config())
    if answer2 : #if they select OK, the canges will commit
        committing_status()
        device.commit_config()
    else: #if they select cancel, the configuration will be discarded
        discarding_status()
        device.discard_config()
    
    # Close session with device:
    device.close()
    answer3 = showinfo("Done", message=done_status()) 
    if answer3 : #if they select OK
        master.destroy() #close the status GUI box
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        #print('Please supply the full path to "new_good.conf"')
        path_status() #push message to status GUI box
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)
