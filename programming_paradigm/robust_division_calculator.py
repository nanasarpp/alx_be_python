def safe_divide(numerator,denominator):
    try:
    #    float(numerator)
    #    float(denominator)
       result = float(numerator) /float(denominator)
       return f"The result of the divison is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
