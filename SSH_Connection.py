import sys
import threading
import time
import concurrent.futures
import paramiko
import concurrent.futures

port = 22  # a varible to hold the SSH port number
username = 'khalil'  # a variable to hold the username ( same for all my Hosts) the username to authenticate as
password = 'khalil'  # a variable to hold the username ( same for all my Hosts) used for password authentication
cmd = 'python3 Khalil.py '  # a variable to hold the command prefix
codepath = '/Khalil.py'  # a variable to hold the code file path


def create_host_tree(ipanddir, cmd, username, password):  # declaring the method
    time.sleep(0.000001)
    ip, dir = ipanddir.split("|")
    ssh = paramiko.SSHClient()  # Create a new SSHClient
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  # Set policy to use when connecting to servers without a known host key
    ssh.connect(ip, port, username, password,
                allow_agent=False,  # set to False to disable connecting to the SSH agent (Forwarding)
                timeout=2000000)  # Connect to an SSH server and authenticate to it
    # timeout=2000000 an optional timeout (in seconds) for the TCP connec
    sftp = ssh.open_sftp()  # Open an SFTP session on the SSH server.Returns:	a new SFTPClient session object
    # sftp==> Used to open an SFTP session across an open SSH Transport and perform remote file operations
    sftp.put(remotepath=dir + codepath,
             # remotepath. the destination path on the SFTP server. Note that the filename should be included
             localpath='K:\Alpha-Team\BmcInterView' + codepath)  # Copy a local file (localpath) to the SFTP server as
    start = time.perf_counter()
    # print('thread ', thread.ident, 'has started')
    start_time = time.time()
    stdin, stdout, stderr = ssh.exec_command('cd ' + dir + ';' + cmd + '"' + ip + '|' + dir + '"',
                                             # Execute a command on the SSH server.
                                             get_pty=True)  # request a pseudo-terminal from the server (default False). See Channel.get_pty
    # the stdin, stdout, and stderr of the executing command, as a 3-tuple
    stdin.close()  # Close the channel. All future read/write operations on the channel will fail
    # close this SSHClient and its underlying Transport.

    for line in stdout:
        print(ip + '' + line.strip('\n'))

    ssh.close()
    data = ip + ' printed thread number:' + str(threading.get_ident()) # print the thread id
    print(data)
    print("--- %s seconds ---" % (time.time() - start_time))


i = 0
threads = []
input = sys.argv[1]
threads_arguments = input.split(",")
print(threads_arguments)
# for argument in threads_arguments:

with concurrent.futures.ThreadPoolExecutor() as executor:  # defining the thread executor
    result = [executor.submit(create_host_tree, argument, cmd, username, password) for argument in
              threads_arguments]  # iterating over the argument and sending them to activate the shell commands
    # executing the threads

    for f in concurrent.futures.as_completed(result):  # for the results from the threads as when they are complete print
        print(f.result())


