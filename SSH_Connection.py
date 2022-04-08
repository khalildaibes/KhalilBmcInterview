import sys
import threading
import time
from threading import Thread
import concurrent.futures
import paramiko
#python simple.py "Host3|/home/khalil/Desktop" ===>to run from the terminal.
port = 22
username = 'khalil'
password = 'khalil'
dir = '/home/khalil/Desktop'
cmd = 'python3 main.py '
codepath = '/main.py'
printedfilename = ''
lock = threading.Lock()
def create_host_tree(ip, cmd, dir, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, allow_agent=False, timeout=2000000)
    sftp = ssh.open_sftp()
    print(ip, "   ", dir, " ", codepath, "   ",'K:\Alpha-Team\khalilBmcInterview\\' + codepath )
    sftp.put(remotepath=dir + codepath, localpath='K:\Alpha-Team\khalilBmcInterview' + codepath)

    stdin, stdout, stderr = ssh.exec_command('cd '+dir+';' + cmd + '"' + ip + '|' + dir + '"',
                                             get_pty=True)
    stdin.close()

    while True:
        printedfilename = stdout.readline()
        print(str(printedfilename))
        if stdout.channel.exit_status_ready():
            break

    ssh.close()



threads = []
input = sys.argv[1]
threads_arguments = input.split(",")
print(threads_arguments)
for argument in threads_arguments:
    ip, dir = argument.split("|")
    print(ip, "   ", dir)
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(create_host_tree, ip, cmd, dir, username, password)

