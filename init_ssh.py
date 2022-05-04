import paramiko
import time

def initial_config():
    # creating an ssh client object
    ssh_client = paramiko.SSHClient()
    print(type(ssh_client))
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='10.10.10.1', port='22', username='cisco:1', password='cisco',
                    look_for_keys=False, allow_agent=False)
    print('Connected to 10.10.10.1')


    # checking if the connection is active
    print(ssh_client.get_transport().is_active())

    # creating a shell object
    shell = ssh_client.invoke_shell()

    print('sending commands')
    # sending commads to the remote device to execute them
    # each command ends  in \n (new line, the enter key)
    shell.send('\r\n')
    shell.send('no\n')
    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('conf t\n')
    shell.send('hostname S1\n')
    shell.send('ip domain name menards.com\n')
    shell.send('ip ssh ver 2\n')
    shell.send('crypto key generate rsa\n')
    # time.sleep(1)
    # shell.send('yes\n')
    time.sleep(1)
    shell.send('1024\n')
    time.sleep(3)
    shell.send('username cisco privilege 15 secret cisco\n')
    shell.send('line vty 0 4\n')
    shell.send('transport input all\n')
    shell.send('session-timeout 60\n')
    shell.send('exec-timeout 60\n')
    shell.send('password cisco\n')
    shell.send('login local\n')
    shell.send('int vlan 1\n')
    shell.send('ip add 10.10.10.10 255.255.255.0\n')
    shell.send('no shut\n')
    shell.send('exit\n')
    shell.send('ip scp server enable\n')
    shell.send('archive\n')
    shell.send('path flash:backup\n')
    shell.send('do wr\n')
    shell.send('exit\n')
    shell.send('exit\n')

    #shell.send('show ip int brief\n')
    time.sleep(2)  # waiting for the remove device to finish executing the commands (mandatory)

    print('Closing connection')
    ssh_client.close()