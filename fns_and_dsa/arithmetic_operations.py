def perform_operation(num1, num2, operation):
    if operation == "add":
       return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
             return "Cant perform operation"
            
        else:
           return num1/num2
    else:
        return "Enter a valid operation"
    