# Import libraries
import os
import threading
import time
from termcolor import colored

# Insert the directory path in here
from threading import Thread


def add_element(dict, key, values):
    if key not in dict:
        dict[key] = []
    dict[key].append(values)


def print_dir_content(path, fileslst, folderslst, parent, spaces, parentspaces):
    # Extracting all the contents in the directory corresponding to path
    l_files = os.listdir(path)
    count = 0
    filescount = 0
    for file in l_files:
        file_path = f'{path}\\{file}'
        if os.path.isfile(file_path):
            count += 1

    # Iterating over all the files in the dir
    for file in l_files:
        filescount += 1
        filespaces = (int(spaces) ) * "─"
        parentspacesstr = (int(parentspaces)) * " "
        parentsprespaces=(int(spaces) ) * " "
        # Instantiating the path of the file
        file_path = f'{path}\\{file}'
        is_last = count == len(l_files)
        # Checking whether the given file print it
        if os.path.isfile(file_path):
            try:
                # Printing the file pertaining to file_path
                if filescount == count:
                    add_element(fileslst, f'|{parentspacesstr}|{parent}',
                                [f'|{parentsprespaces} |{parentspacesstr}|{filespaces}└{file}', spaces, spaces + parentspaces])

                else:
                    add_element(fileslst, f'|{parentspacesstr}|{parent}',
                                [f'|{parentsprespaces} |{parentspacesstr}|{filespaces}├{file}', spaces, spaces + parentspaces])
            except:
                # Catching if any error occurs and alerting the user
                print(f'ALERT: {file} could not be printed! Please check\
                the associated softwares, or the file type.')

    # Iterating over all the files in the dir
    for file in l_files:

        # Instantiating the path of the file
        file_path = f'{path}\\{file}'
        folderspaces = (int(spaces)) * ""
        parentspacesstr = int(parentspaces) * ""
        # Checking whether the given file is a directory
        if not (os.path.isfile(file_path)):
            folderslst.append(f'└{parentspacesstr}|{folderspaces}├{file}')
            thread = Thread(target=print_dir_content,
                            args=(
                                file_path, fileslst, folderslst, file_path, int(spaces + 1),
                                int(spaces + parentspaces)))
            thread.start()
            thread.join()


lst = [r"HOST1|C:\Users\Admin\Desktop\zero-to-mastery\jstest", r"HOST2|C:\Users\Admin\Desktop\Android",
       r"HOST3|C:\Users\Admin\Desktop\projectBeta3.0", r"HOST1|C:\Users\Admin\Desktop\DM_PROJECT_GROUP_12 (1)"]

# n = int(input("Enter number of Hosts : "))
# lst = []
# # iterating till the range
# for i in range(0, n):
#     ele = str(input("Please neter in this fromat HostName|Requested root directory  "))
#     lst.append(ele)  # adding the element


for el in lst:
    folderslst = []
    fileslst = {}
    txt = str(el)
    x = txt.split("|")
    x[1].replace(r'\\', '/')
    thread = Thread(target=print_dir_content, args=(x[1], fileslst, folderslst, x[1], 1, 0))
    thread.daemon = True
    thread.start()
    thread.join()
    print(colored(('=>the host name is **', x[0], '**   the requested dir is **', x[1], 'the trhraed id', thread.ident,
                   '** <='), 'blue'))

    for elm in fileslst:
        spaces = fileslst.get(elm)[0][1] * " "
        print(colored(f'└{spaces} {elm}', 'red'))
        for filelst1 in fileslst.get(elm):
            print(colored(f'{filelst1[0]}', 'green'))
