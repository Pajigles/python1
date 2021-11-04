##PJ Frost
##Programming Assignment 7
##11/04/2021
##SEC.207
import re
import os


def osname():
    result = os.name
    if re.match("nt", result):
        print("This is a windows operating system")
    if re.match("posix", result):
        print("This is a mac or linux operating system")

def checkaccess():
    result = os.access("/users/",os.F_OK)
    result = str(result)
    if re.search("True", result):
        print("Access to C:/users is True")
    else:
        print("Access to C:/users is False")

def returncwd():
    result = os.getcwd()
    if re.fullmatch(r"C:\\Users\\PJ\\PycharmProjects\\python1", result):
        print("This directory exists")
    else:
        print("This directory does not exist")

if __name__ == '__main__':
    osname()
    print()
    checkaccess()
    print()
    returncwd()