#Validate that the device has the following configured properly:
# -Vlan 1 shut down
# -Correct Interfaces
# -Trunk Ports
# -SSH keys
import napalm
import pprint
import json

ios_driver = napalm.get_network_driver('ios')
ios_config = {
    "hostname": "switch1",
    "username": "cisco",
    "password": "cisco",
    "optional_args": {"secret": "cisco"}
}

with ios_driver(**ios_config) as ios:
    pprint.pprint(ios.compliance_report("errorCheck.yaml"))

