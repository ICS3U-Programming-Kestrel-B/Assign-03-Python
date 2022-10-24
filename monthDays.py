#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 19, 2022
# This program asks for a month and
# year and tells the user how many
# days are/were in that month

import math

def main():
    # introductory paragraph
    print("This program asks for a month and")
    print("year and tells the user how many")
    print("days are/were in that month")
    print("(Leap years are accounted from 2000")
    print("to present day)")
    print("")
    # input
    # getting user_month
    user_month = input("Enter a month: ")

    # getting year
    user_year = int(input("Enter a year: "))

    # process/output
    # giving value to month_num
    if user_month == "January":
        month_num = 31;
    elif user_month == "February":
        month_num = 29;
    elif user_month == "March":
        month_num = 31;
    elif user_month == "April":
        month_num = 30;
    elif user_month == "May":
        month_num = 31;
    elif user_month == "June":
        month_num = 30;
    elif user_month == "July":
        month_num = 31;
    elif user_month == "August":
        month_num = 31;
    elif user_month == "September":
        month_num = 30;
    elif user_month == "October":
        month_num = 31;
    elif user_month == "November":
        month_num = 30;
    elif user_month == "December":
        month_num = 31;
    else:
        print("An irregularity has occurred.\n")
        print("Please enter a valid month.\n")
        print("Try checking your spelling.")

    # output
    # checking if year is a leap year
    if user_month == "February":
        if user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    # is a leap year
                    print(("{} is a leap year,").format(user_year))
                    print(("so {} has 29 days.").format(user_month))
                else:
                    # is not a leap year
                    print(("{} has ").format(user_month))
                    print(("{} days in ").format(month_num))
                    print(("{}.").format(user_year))
            else:
                # is a leap year
                print(("{} is a leap year,").format(user_year))
                print(("so {} has 29 days.").format(user_month))
        else:
            # is not a leap year
            print(("{} has ").format(user_month))
            print(("{} days in ").format(month_num))
            print(("{}.").format(user_year))
    else:
        # is not a leap year
        print(("{} has ").format(user_month))
        print(("{} days in ").format(month_num))
        print(("{}.").format(user_year))



if __name__ == "__main__":
    main()
