##PJ Frost
##Programming Assignment 5 (hashlib)
##10/19/2021
##SEC.207
import hashlib

def hash256(plaintext):
    hash = hashlib.sha256(plaintext.encode())
    sha256 = hash.hexdigest()
    print(sha256)

if __name__ == '__main__':
    plaintext = input("Enter your password to be hashed: ")
    hash256(plaintext)