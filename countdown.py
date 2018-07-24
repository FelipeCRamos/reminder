#!/usr/bin/env python3

"""
Author: FelipeCRamos
"""

import sys
import datetime

def form_title():
    """
    This will form the title, getting all the titles on:
    ./countdown.py DD/MM/YYYY [title] [second title] [ third title ] ...

    * adding a space between them
    """
    size = len(sys.argv)
    title = str()
    for i in range(2, size):
        title += sys.argv[i]
        if( i != size - 1 ):
            title += " "
    return title

def form_date(date_string):
    """
    Getting a kind of regex on the date_string, getting the datetime object
    DD/MM/YYYY
    """
    try:
        real_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
    except:
        print("Incorrect date format, please rerun with the format DD/MM/YYYY!")
        exit()
    return real_date.date()

# Escape sequences (make code simple)
blue_bold = "\033[36;1m"
normal = "\033[0m"

# Main

if(len(sys.argv) >= 3):
    try:
        # if the sys.argv got success

        # forms the title
        date_title = form_title()

        # get's today info
        today = datetime.date.today()

        # get's desired date
        foward_date = form_date(sys.argv[1])

        # makes the difference between them
        diff = (foward_date - today).days

        # showcase the result in a pretty way
        print("> {}{:0>3}{} days | "
              "{}{:0>5.2f}{} weeks | "
              "{}{:0>5.2f}{} months "
              "-> {}!".format(
                  blue_bold, diff, normal,
                  blue_bold, diff / 7, normal,
                  blue_bold, diff / 30, normal,
                  date_title))
    except Exception as exp :
        print("Ops, didn't saw that coming...")
        print("Error: {}".format(exp))
        print("Please, feel free to drop that exception on my github page!")
        exit()

else:
    if( len(sys.argv) == 2 ):
        print("\n\nYou forgot the title for the countdown!\n")
    # wrong parameters
    print("Please, (re)run the program with needed parameters!")
    print("\nex:\t./countdown.py 10/1/2019 Math Test\n\n")
