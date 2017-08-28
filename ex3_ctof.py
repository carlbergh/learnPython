# Write program to convert celcius to fahrenheit
#temp_in_celcius = 0
#temp_in_fahrenheit = 0
menu_option = -1
menu_options = [0, 1, 2]

# Define functions here
def main_menu (option):
    if option == 1:
        celcius_to_fahrenheit();
    elif option == 2:
        fahrenheit_to_celcius();
    else:
        end_program()

def end_program():
    print "\n Ending this fantastic program! Have a nice day!\n"
    exit(0)

def value_checker():
    inputt = raw_input(" Enter degrees: ")

    try:
        return float(inputt)
    except ValueError:
        print "Please enter a valid number"
        return value_checker()

def celcius_to_fahrenheit ():
    print "\nThis function will convert from Celcius to Fahrenheit"

    while True:
        temp_in_celcius = value_checker()
        break

    # Calculate Fahrenheit
    fahrenheit = float(temp_in_celcius) * 9.0 / 5.0 + 32

    print "Temperature: "
    print "Celcius: ", temp_in_celcius
    print "Fahrenheit: ", fahrenheit
    return fahrenheit

def fahrenheit_to_celcius ():
    print "\nThis function will convert from Fahrenheit to Celcius"

    while True:
        temp_in_fahrenheit = value_checker()
        break    # Calculate Celcius
    celcius = (temp_in_fahrenheit-32) * 9.0 / 5.0

    print "Temperature: "
    print "Celcius: ", celcius
    print "Fahrenheit: ", temp_in_fahrenheit
    return celcius

### Main program ###

while menu_option not in menu_options:
    print "\n MAIN menu\n"
    print " 0. Exit program"
    print " 1. Convert Celcius to Fahrenheit"
    print " 2. Convert Fahrenheit to Celcius"
    menu_option = input('\n Enter Option: ')

main_menu(menu_option)
