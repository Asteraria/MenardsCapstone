#!/bin/bash
#ssh-keygen 
#ssh cisco@10.10.10.10 -o "StrictHostKeyChecking no"
sshpass -p "cisco" ssh -o "StrictHostKeyChecking no" cisco@10.10.10.10 'exit'
exit 1