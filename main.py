##PJ Frost
##Programming Assignment 6 Strings3
##10/29/2021
##SEC.207


def function1(sentence):
    for words in sentence.split():
        print(words)


def function2(sentence):
    for words in range(len(sentence)):
        print(sentence[words])



if __name__ == "__main__":
    print("Enter a sentence to be split:" )
    sentence =  input()
    function1(sentence)
    print(" ")
    function2(sentence)
