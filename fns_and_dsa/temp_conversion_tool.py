FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def  convert_to_celsius():
    
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    global conversion
    conversion =  FAHRENHEIT_TO_CELSIUS_FACTOR *( temp - 32)
    # return conversion 
    print(f"{temp}°F is {conversion}°C")

def convert_to_fahrenheit():
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    global conversion 
    conversion  = (CELSIUS_TO_FAHRENHEIT_FACTOR *temp )+ 32 
    print(f"{temp}°C is {conversion}°F")


temp = float(input("Enter the temperature to convert: "))
degrees = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if degrees == "C":
    convert_to_fahrenheit()
elif degrees == "F":
    convert_to_celsius()