import os
from time import sleep
from threading import Thread

exelist = ['printer.exe', 'Printer.exe', 'PRINTER.exe']

def printer(path = os.getcwd()):
    for file in os.listdir(path):
        if file not in exelist:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.startfile(file, "print")
                sleep(9)
            else:
                printer(file_path)
    delete(path)

def delete(path = os.getcwd()):
    for file in os.listdir(path):
        if file not in exelist:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

printer()