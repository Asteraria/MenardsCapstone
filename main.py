# Main Application 
import GUI
import load_replace as LR
import ansible_runner as AR
import init_ssh as IS
import subprocess

GUI.userPrompt1()

GUI.runningScript('Initial Config')
IS.initial_config()
GUI.success('Initial Config')

GUI.runningScript('Reset SSH')
subprocess.call('./reset.sh')
GUI.success('Reset SSH')

# Run IOS Check/Upgrade Script
GUI.runningScript('IOS Check/Upgrade')
AR.run(playbook='/home/ansible/Desktop/Menards_Scripts2/IOS_Check.yaml')
GUI.success("IOS Check/Upgrade")

# Select file to run load/replace script
path = GUI.selectFile()
LR.main(path)
GUI.success("Load/Replace")

# Run Validation Script
GUI.runningScript('Validation')

AR.run(playbook='/home/ansible/Desktop/Menards_Scripts2/validate_configuration.yaml')
GUI.success("Validation")