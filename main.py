##PJ Frost
##Programming Assignment 5 (datetime)
##10/19/2021
##SEC.207
from datetime import datetime

def todaytime():
    time = datetime.time(datetime.now())
    print("The current time is", time)

def todaydate():
    date = datetime.date(datetime.today())
    print("The date today is", date)


if __name__ == '__main__':

    option = int(input("Press 1 for the time and 2 for the date or 3 for both: "))
    if option == 1:
        todaytime()

    if option == 2:
        todaydate()

    if option == 3:
        todaytime()
        todaydate()

