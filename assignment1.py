#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
Joanne Kuang. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Joanne Kuang
Semester: Fall 2024
Description: Assignment 1 Version B 
'''

import sys

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    # check for leap year
    four = year % 4
    hundred = year % 100
    fourhundred = year % 400

    if four == 0: 
        if hundred != 0: 
            return True
        elif fourhundred == 0:
            return True
    return False 

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    # show the end of each day of each month
    num_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month == 2: # this will check for feburary
        if leap_year(year): 
            return 29 # leap year will return
        return 28 # not a leap year

    month = month - 1 # for the 0 index for num_days
    return num_day[month] # this will return the other months 

def after(date: str) -> str: 
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day= (int(x) for x in date.split('-'))
    day = day + 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon = mon + 1
        if mon > 12:
            year = year + 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    "Returns previous day's date as YYYY-MM-DD"
    year, mon, day= (int(x) for x in date.split('-'))
    day = day - 1  # previous day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # if this is feb and if its a leap year
    if mon == 2 and leap_flag:
        mon_max = 29 # leap = 29
    else:
        mon_max = mon_dict[mon] # if not a leap year
    
    # if the day goes -1 then change the month and the year
    if day < 1:
        mon = mon - 1 # this will move into previous month
        if mon < 1: # if this month goes before jan then go down one year
            mon = 12 # months
            year = year - 1 # this will go to previous year
        day = mon_dict[mon]  # this will get the last day of each month 

        # change to also include feb for leap year
        if mon == 2:
            if leap_flag:
                day = 29 # if this is a leap year 
            else:
                day = 28 # if not a leap year

    return f"{year}-{mon:02}-{day:02}"


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

    # user will need to input 3
    if len(sys.argv) != 3:
       print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
       sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    # this will check for the valid date YYYY-MM-DD
    try:
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)

        # this will check if the month is valid 
        if month < 1:
            return False
        if month > 12:
            return False

        # get the max day given month and year
        maxday = maxmonth(month, year)

        # this will check if the day is valid
        if day < 1:
            return False
        if day > maxday:
            return False

        return True
    except:
        return False

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    # caculate date 
    date = start_date

    if days > 0:
        date = after(date)
        days = days - 1
    elif days < 0:
        date = before(date)
        days = days + 1

    return date

if __name__ == "__main__":
    # check correct input provided
    if len(sys.argv) != 3:
        print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
        usage()

    # must valid the start of the date
    start_date = sys.argv[1]
    valid = valid_date(start_date)
    if valid == False:
        print("Error: Invalid date format")
        usage()

    try:
        days = int(sys.argv[2])
    except ValueError:
        usage()

    if int(sys.argv[2]) == 0:
        usage()

    # calculate the number of days with /
    daysyears = 365
    days = roundup (daysyears / int(sys.argv[2]))
    print("A year divided by " +sys.argv[2] + " is " + str(days) + " days. ")

    # calculate the date NN with before and after the star date
    beforeday = dbda(start_date, -days)
    nextday = dbda(start_date, days)

    # print the reults
    print("The date " + str(days) + "days ago was " + beforeday + ".")
    print("The date " + str(days) + "days from now will be " + nextday + ".")
