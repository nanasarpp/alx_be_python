first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        if second_number == 0:
           result = "You can not divide by a zero"
           
        else:
            result = first_number/second_number
print(f"The result is {result}")
            
            



