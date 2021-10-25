import os
from time import sleep

file_list = []
file_path = []
printed_path = []

exelist = ["printer.exe", "Printer.exe", "PRINTER.exe", "printer.py"]


def get_branches(path=os.getcwd()):
    print(path)
    global file_list, file_path, count
    for path_to, directories, files in os.walk(path):
        for directory in directories:
            get_branches(os.path.join(path_to, directory))
        for file in files:
            if file and file not in exelist:
                file_list.append(file)
                file_path.append(os.path.join(path_to, file))


def delete(path=os.getcwd()):
    for file in os.listdir(path):
        if file not in exelist:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


def print_leaves():
    global file_dict, printed_path
    count = 0
    file_list.sort()
    for file in file_list:
        for filepath in file_path:
            a = filepath.split("\\")[-1]
            if file == a and filepath not in printed_path:
                printed_path.append(filepath)
                # count += 1
                os.startfile(filepath, "print")
                sleep(2)
                # print(filepath)
    # print(count)


get_branches()
print_leaves()
