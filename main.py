##PJ Frost
##Programming Assignment 8
##11/29/2021
##SEC.207


class Bird:

    mouth = "beak"
    travelby = "flying"

    def __init__(self, name):
        self.name = name

    def lay_egg(self):
        print("An egg was laid by {}".format(self.name))


print("Enter name of first bird: ")
inputone = input()

print("Enter name of second bird: ")
inputtwo = input()

Bird1 = Bird(inputone)
Bird2 = Bird(inputtwo)

Bird1.lay_egg()
Bird2.lay_egg()

print(dir(Bird1))
print(dir(Bird2))