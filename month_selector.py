#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user input an integer from 1-12 and tells them what month it is


def main():
    # this function lets the user enter an integer from 1-12
    #   and returns a month that corresponds that that number
    
    # input
    print("Entering an integer will tell you a month.")
    month = input("Enter an integer between 1-12: ")

    # process & output
    try:
      month_int = int(month)
      
      if month_int > 12:
        print("\nThe integer you inputted is too large!") # No month 13
      
      elif month_int < 1:
        print("\nThe integer you inputted is too small!") # No month 0 or negative months

      elif month_int == 1:
        print("\nYour month is January!")

      elif month_int == 2:
        print("\nYour month is Feburary!")

      elif month_int == 3:
        print("\nYour month is March...") # Sister's birthday is in March therefore its the worst month

      elif month_int == 4:
        print("\nYour month is April!")

      elif month_int == 5:
        print("\nYour month is May!")

      elif month_int == 6:
        print("\nYour month is June!")

      elif month_int == 7:
        print("\nYour month is July!")

      elif month_int == 8:
        print("\nYour month is August!!") # My birthday is in August therefore its the best month

      elif month_int == 9:
        print("\nYour month is September!")

      elif month_int == 10:
        print("\nYour month is October!")

      elif month_int == 11:
        print("\nYour month is November!")

      elif month_int == 12:
        print("\nYour month is December!")

    except Exception:
      print("\nYou have entered an invalid string.")
    finally:
      print("\nDone")

if __name__ == "__main__":
    main()
    