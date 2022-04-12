# Nampalm Load Config Script
# Written by Grant Bruehl 3/31/22
from __future__ import print_function

import napalm
import sys
import os

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

    print("Opening...")
    device.open()

    print("Loading replacement candidate...")
    device.load_replace_candidate(filename=config_file)

    # Note: Config has not been applied at this point
    # Prompt user to commit or discard changes:
    print("\nDifferences:")
    print(device.compare_config())

    try: 
        choice = input("\nWould you like to commit these changes? [y/N]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [y/N]: ")
    if choice == "y":
        print("Committing ...")
        device.commit_config()
    else:
        print("Discarding ...")
        device.discard_config()
    
    # Close session with device:
    device.close()
    print("Done.")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please supply the full path to "new_good.conf"')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)
