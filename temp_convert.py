#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 1st, 2023
# this program converts from degrees Celcius to Fahrenheit and Kelvin.


def main():
    # user inputs degrees Celsius to the user.
    try:
        celsius = float(input("Enter degrees in Celsius: "))
        # terminal will process converting from Celsius to Fahrenheit and Kelvin
        fahrenheit = celsius * 9 / 5 + 32
        kelvin = celsius + 273.15
    # terminal will give an error if the input is not a number
    except ValueError:
        print("Error, please enter a valid numerical value for degrees Celsius.")
    # terminal will display the degrees Celsius and the degrees Fahrenheit and Kelvin
    else:
        print("The temprature in Celsius is = {} degrees".format(celsius))
        print("The temperature in Fahrenheit is = {} degrees".format(fahrenheit))
        print("The temperature in Kelvin is = {} degrees".format(kelvin))


if __name__ == "__main__":
    main()
