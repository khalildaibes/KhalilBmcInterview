# -*- coding: utf-8 -*-

import os  # importing os module to use os.listdir(path)
import time  # importing time module
import sys  # importing os module to use argv

filenames = []
start_time = time.time()
lst = []
ele = sys.argv[1]  # receiving the input form (Terminal)
lst.append(ele)  # adding the element


def print_dir_content(path, parent, spaces, parentspaces):
    # Extracting all the contents in the directory corresponding to path
    l_files = os.listdir(path)
    # variables for customization of the printing process
    file_spaces = (int(spaces)) * "─"
    parents_pre_spaces = (int(parentspaces + spaces)) * " "
    parents_spaces = (int(spaces)) * " "
    # Iterating over all the files

    for file in l_files:

        # Instantiating the path of the file
        file_path = '' + path + '/' + file  # initialization the file path name

        # Checking whether the given file is a file or not
        if os.path.isfile(file_path):
            print(
                '|' + parents_pre_spaces + '|' + parents_spaces + '|' + file_spaces + '  └' + file_path)  # printing the file
        # Checking whether the given file is a directory or not
        elif os.path.isdir(file_path):
            try:
                print(
                    '|' + parents_pre_spaces + '|' + parents_spaces + parent + '\\' + file_path)  # printing the directory
                print_dir_content(file_path, parent, spaces + 1, spaces + parentspaces + 1)
            except:
                pass  # do nothing


for el in lst:

    fileslst = {}  # dictionary to hold the
    txt = str(el)  # converting the argv to string
    x = txt.split("|")  # splitting the input to 2
    x[1].replace(r'\\', '/')
    thstart_time = time.time()  # get the starting time
    print_dir_content(x[1], x[0], 0, 1)  # calling the method
    print('\n ' + str(time.time() - thstart_time))  # printing elapsed time

