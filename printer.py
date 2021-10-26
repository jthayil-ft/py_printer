import os
from time import sleep

file_path = []
exelist = ["printer.exe", "Printer.exe", "PRINTER.exe", "printer.py"]


def get_branches(path="C:\\SAP\\Digi_Sign\\Print"):
    global file_list, file_path, count
    for path_to, directories, files in os.walk(path):
        for directory in directories:
            get_branches(os.path.join(path_to, directory))
        for file in files:
            if file and file not in exelist:
                file_path.append(os.path.join(path_to, file))


def print_leaves():
    global file_path
    count = 0
    file_path.sort()
    for file in file_path:
        count += 1
        try:
            os.startfile(file, "print")
        except:
            pass
        sleep(3.5)
        print(file)
    print(count)


get_branches("C:\\SAP\\Digi_Sign\\Print")
print_leaves()
