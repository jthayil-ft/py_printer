import logging
import os
import shutil
from threading import Thread
from time import sleep

PRODUCTION = True
LOGFILE = 'C:\\SAP\\Digi_Sign\\ftspl.log'

try:
    if os.path.isfile(LOGFILE):
        os.remove(LOGFILE)
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                        filename=LOGFILE, encoding='utf-8', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
except Exception as e:
    logging.critical('\nException : \t' + str(e) + '\n')


def build_index(dir_struct, path="C:\\SAP\\Digi_Sign\\Print"):
    count = 0
    for path_to, directories, files in os.walk(path):
        for directory in directories:
            logging.debug('\nReading Directory \t' + str(path_to) + '\n')
            Thread(target=build_index, args=[
                dir_struct, os.path.join(path_to, directory)])
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            logging.debug('\nfileName \t' + str(file_name) +
                          str(file_extension) + '\n')
            if file and file_extension == ".pdf":
                count += 1
                dir_struct[file_name] = os.path.join(path_to, file)
                logging.debug('\ncount \t' + str(count) +
                              '\t filesDict \n' + str(dir_struct) + '\n')
    return dir_struct, count


def movefile(filepath, filename):
    move = True
    while move:
        try:
            shutil.move(filepath, "C:/SAP/Digi_Sign/Success/" + str(filename) + ".pdf")
            logging.info('\nFile processed for moving \t' + str(filepath) + '\n')
            move = False
        except Exception:
            sleep(3)
            Thread(target=movefile, args=[filepath, filename]).start()
            logging.info('\nException Retrying \t' + str(filepath) + '\n')


def main():
    last_scan = -1
    lastrun = 0
    dir_struct = {}
    try:
        while lastrun > last_scan:
            last_scan = lastrun
            dir_struct, lastrun = build_index({}, "C:\\SAP\\Digi_Sign\\Print")
            if PRODUCTION:
                sleep(10)
            logging.info('\nFile Count \t' + str(lastrun) + '\n')

        logging.info('\nBefore Sorting\t' + str(dir_struct) + '\n')
        z = {int(k): v for k, v in dir_struct.items()}
        j = dict(sorted(z.items(), key=lambda x: x[0]))
        logging.info('\nAfter Sorting\t' + str(j) + '\n')

        # Start Printing Process
        for k, val in j.items():
            try:
                logging.info('\nFile send for printing \t' + str(val) + '\n')
                os.startfile(val, "print")
                if PRODUCTION:
                    sleep(8)
                    Thread(target=movefile, args=[val, k]).start()
            except Exception as e:
                logging.critical('\nException : \t' + str(e) + '\n')

    except Exception as f:
        logging.critical('\nException : \t' + str(f) + '\n')


if __name__ == "__main__":
    main()
