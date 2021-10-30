##PJ Frost
##Programming Assignment 6 Strings1
##10/29/2021
##SEC.207
import sys


def function1():
    fun1 = sys.argv
    print(f"Make string upper: {fun1}")
    for i, arg in enumerate(fun1):
        print(f"Argument {i:>6}: {arg.upper()}")

def function2():
    fun2 = sys.argv
    print(f"Make string {fun2}")
    for i, arg in enumerate(fun2):
        print(f"Argument {i:>6}: {arg.swapcase()}")

if __name__ == "__main__":
    function1()
    function2()