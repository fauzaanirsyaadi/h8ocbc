# function to convert the celcius to kelvin
def convert(celsius):
    kelvin = celsius + 273.15
    return kelvin


# function to convert the kelvin to celsius
def convert2(kelvin):
    celsius = kelvin - 273.15
    return celsius


# function to convert the kelvin to fahrenheit and give arguments to check the input
def convert3(kelvin):
    if kelvin < -273.15:
        print("The value is not possible to convert")
    else:
        fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
        return fahrenheit


# function to convert the celsius to fahrenheit and give arguments to check the input
def convert4(celsius):
    # check input is not kelvin
    if celsius < -273.15:
        print("The value is not possible to convert")
    # check input is not nulls
    elif celsius == 0:
        print("The value is not possible to convert")
    # check input is not fahrenheit
    elif -273.15 < celsius < -459.67:
        print("The value is not possible to convert")
    else:
        fahrenheit = (celsius - 273.15) * 9 / 5 + 32
        return fahrenheit


# function to convert the fahrenheit to kelvin and give documentation to check the anf arguments to check the output
def convert5(fahrenheit):
    if fahrenheit < -459.67:
        print("The value is not possible to convert")
    else:
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        if kelvin < -273.15:
            print("The value is not possible to convert")
        else:
            return kelvin


# function to convert the fahrenheit to Celsius and give arguments to check the output is celsius
def convert6(fahrenheit):
    if fahrenheit < -459.67:
        print("The value is not possible to convert")
    else:
        celsius = (fahrenheit - 32) * 5 / 9
        # check the output is not kelvin
        if celsius < -273.15:
            print("The value is not possible to convert")
        else:
            return celsius


# life cycle function, input, and documentation
def main():
    print("This program converts the temperature from celsius to kelvin and kelvin to celsius")
    print("This program also converts the temperature from celsius to fahrenheit and fahrenheit to celsius")
    print("This program also converts the temperature from kelvin to fahrenheit and fahrenheit to kelvin")
    print("Please enter the temperature in celsius")
    celsius = float(input())
    print("The temperature in kelvin is: ", convert(celsius))
    print("Please enter the temperature in kelvin")
    kelvin = float(input())
    print("The temperature in celsius is: ", convert2(kelvin))
    print("Please enter the temperature in fahrenheit")
    fahrenheit = float(input())
    print("The temperature in celsius is: ", convert3(fahrenheit))
    print("Please enter the temperature in fahrenheit")
    fahrenheit = float(input())
    print("The temperature in kelvin is: ", convert5(fahrenheit))
    print("Please enter the temperature in celsius")
    celsius = float(input())
    print("The temperature in fahrenheit is: ", convert4(celsius))
    print("Please enter the temperature in fahrenheit")
    fahrenheit = float(input())
    print("The temperature in kelvin is: ", convert6(fahrenheit))


# run main function
main()
