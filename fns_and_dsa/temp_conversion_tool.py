FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def  convert_to_celsius():
    
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    global conversion
    conversion =  conversion = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    # return conversion 
    print(f"{temp}°F is {conversion}°C")

def convert_to_fahrenheit():
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    global conversion 
    conversion = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temp}°C is {conversion}°F")


try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
degrees = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if degrees == "C":
    convert_to_fahrenheit()
elif degrees == "F":
    convert_to_celsius()
else:
    print("Invalid temperature. Please enter a numeric value")