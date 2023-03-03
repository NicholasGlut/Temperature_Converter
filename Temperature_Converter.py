
print("\nThis is a program to convert units of temperature.")

while True:
    # User chooses the starting unit of temperature
    print("\nType EXIT to exit...")
    unit = input("Input F for Farenheit or C for Celsius: ")
    
    # Allows exiting of program
    if unit.upper() == 'EXIT':
        break

    # Checks which unit was selected
    if unit.upper() == "F":
        print("You selected Farenheit.")
    elif unit.upper() == "C":
        print("You selected Celsius.")
    else:
        # error handling
        print("Please select F or C...")
        unit = input()

    # Applies temperature conversion
    while True:
        if unit.upper() == "F":
            temp = int(input("Please input temperature Farenheit: "))
            if str(temp).upper() == 'EXIT':
                break
            print((5/9) * (temp-32))

        elif unit.upper() == "C":
            temp = int(input("Please input temperature Celsius: "))
            if str(temp).upper() == 'EXIT':
                break
            print((9/5)*temp+32)
