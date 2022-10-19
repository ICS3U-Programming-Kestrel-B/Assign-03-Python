#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 19, 2022
# This program asks for a month and
# year and tells the user how many
# days are/were in that month


def main():
    # input
    print("This program asks for a month and")
    print("year and tells the user how many")
    print("days are/were in that month")
    print("(Leap years are accounted from 2000")
    print("to present day)")
    print("")
    user_num = int(input("Enter any integer: "))

    # process/output
    if user_num < 0:
        print("Your number is negative.")
    elif user_num > 0:
        print("Your number is positive.")
    elif user_num == 0:
        print("Your number is zero.")
    else:
        print("An irregularity has occurred.")


if __name__ == "__main__":
    main()
