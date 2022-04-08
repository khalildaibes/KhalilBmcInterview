import sys
import threading
import time
from threading import Thread
import concurrent.futures
import paramiko
Host='Host1'
port = 22
username = 'khalil'
password = 'khalil'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(Host, port, username, password, allow_agent=False, timeout=2000000)
sftp = ssh.open_sftp()

stdin, stdout, stderr = ssh.exec_command('ls',
                                         get_pty=True)
stdin.close()

while True:
    printed = stdout.readline()
    print(str(printed))
    if stdout.channel.exit_status_ready():
        break