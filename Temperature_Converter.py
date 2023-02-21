import unittest

print("\nThis is a program to convert units of temperature.")

while True:
    print("\nType EXIT to exit...")
    print("Input F for Farenheit or C for Celsius: ")
    unit = input()
    
    if unit.upper() == 'EXIT':
        break

    if unit.upper() == "F":
        print("You selected Farenheit.")
    elif unit.upper() == "C":
        print("You selected Celsius.")
    else:
        print("Please select F or C...")
        unit = input()

    if unit.upper() == "F":
        temp = int(input("Please input temperature Farenheit: "))
        print((5/9) * (temp-32))
    elif unit.upper() == "C":
        temp = int(input("Please input temperature Celsius: "))
        print((9/5)*temp+32)
    
