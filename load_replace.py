# Nampalm Load Config Script
# Written by Grant Bruehl 3/31/22
import napalm
import os
import PySimpleGUI as sg

def main(config_file):

   
    layout = [
    [sg.Text("Run Load/Replace Script?\n")], 
    [sg.Button("OK")]
    ]

    window = sg.Window("Load/Replace Script", layout, size=(500,200))

    # Create an event loop
    while True: 
        event, values = window.read()
        # Break is user closes window or presses OK
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK": 
            window.close()
            if not (os.path.exists(config_file) and os.path.isfile(config_file)):
                msg = "Missing or invalid config file {0}".format(config_file)
                raise ValueError(msg)

            sg.Print("Loading config file {0}.".format(config_file))

            # Use the appropriate network driver to connect to device:
            driver = napalm.get_network_driver("ios")

            # Connect:
            device = driver(
                hostname="10.10.10.10", 
                username="cisco", 
                password="cisco", 
                #optional_args= {'secret': "cisco"}
                optional_args={'secret':"cisco", "port":22} #TO BE USED WITH CONSOLE SERVER PORTS 
            )

            sg.Print("Opening...")
            device.open()

            sg.Print("Loading replacement candidate...")
            device.load_replace_candidate(filename=config_file)

            # Note: Config has not been applied at this point
            # Prompt user to commit or discard changes:
            sg.Print("\nDifferences:")
            sg.Print(device.compare_config())

            sg.Print("Committing ...")
            device.commit_config()

            # Close session with device:
            device.close()
            sg.Print("Done.")
    window.close()
    # Create an event loop
    

#main('../Menards_Config_Files/Config.txt')
