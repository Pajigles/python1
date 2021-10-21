##PJ Frost
##Programming Assignment 5 (getpass)
##10/20/2021
##SEC.207
import getpass

def createfile(filename):
    username = getpass.getuser()
    file = open(f'C:\\Users\\{username}\\Desktop\\{filename}.txt','w')
    text = input("Enter information into the file: ")
    file.write(text)
    file.close()


if __name__ == '__main__':
    filename = input("Enter the name of the file: ")
    createfile(filename)