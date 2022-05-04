import PySimpleGUI as sg

# Prompt user to plug in devices
def userPrompt1():
    # Set layout parameters
    layout = [
        [sg.Text("Please Plug in Router/Switch Console Ports to the Console Server. \n\nPress Next to Continue\n")], 
        [sg.Button("Next")]
        ]

    # Create the window
    window = sg.Window("Router/Switch Configuration", layout, size=(500,200))

    # Create an event loop
    while True: 
        event, values = window.read()
        # Break is user closes window or presses OK
        if event == "Next" or event == sg.WIN_CLOSED:
            break
    window.close()

# Startup script status message
def runningScript(script):
    # Set layout parameters
    layout = [
        [sg.Text("Running %s Script...\n" % script)]
        ]

    # Create the window
    window = sg.Window("Router/Switch Configuration", layout, size=(500,200))

    # Create an event loop
    while True:
        event, values = window.Read(timeout = 1000 * 5)  # in milliseconds
        if event in ('__TIMEOUT__',):
            window.close()   
        if event in (sg.WIN_CLOSED,): break
        
def selectFile():
    # Set layout parameters
    layout = [
        [sg.In(key="-FILE-"), sg.FileBrowse(file_types=(("Text Files", "*.txt"),))],
        [sg.Button("Exit"), sg.Button("Submit")],
    ]

    # Create the window
    window = sg.Window("Select a Configuration File", layout, size=(500,200))
   
    # Create an event loop
    while True: 
        event, values = window.read()
        # Break is user closes window or presses OK
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            window.close()
            return(values["-FILE-"])
        window.close()


def success(script):
    # Set layout parameters
    if script == "Validation":
        layout = [
        [sg.Text("%s Script Ran Successfully.\n Trunking is Enabled.\n Cryrpto Key Successfully Created.\n VLAN 1 is Up.\n" % script)]]
    else:
        layout = [
            [sg.Text("%s Script Ran Successfully.\n" % script)]]

    # Create the window
    window = sg.Window("Router/Switch Configuration", layout, size=(500,200))

    # Create an event loop
    while True:
        event, values = window.Read(timeout = 1000 * 5)  # in milliseconds
        if event in ('__TIMEOUT__',):
            window.close()   
        if event in (sg.WIN_CLOSED,): break

