##PJ Frost
##Programming Assignment 6 Strings2
##10/29/2021
##SEC.207

def piglatin(string):
    string = string.split()
    for i in range(len(string)):
        j = string[i]

        if j[0] in ['a','e','i','o','u']:
            string[i] = j + 'yay'

        if j[0] not in ['a','e','i','o','u']:
            if j[0] and j[1] not in ['a','e','i','o','u','y']:
                string[i] = j[1:]+j[0]
                string[i] = j[2:]+j[0] + 'ay'
            else:
                string[i] = j[1:]+j[0] + 'ay'


    print(string)

if __name__ == "__main__":
    string = str(input("Enter a string: "))
    piglatin(string)


