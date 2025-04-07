def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        # TODO: Implement operation handling and raise exceptions for invalid cases
        l=["+","-","/","*","**"]
        if operator not in l:
            return "unsuportted operator"
        if operator=='/':
            return (int(a)/int(b))
        elif operator=='+':
            return (int(a)+int(b))
        elif operator=="-":
            return (int(a)-int(b))
        elif operator=="%":
            return (int(a)%int(b))
        elif operator=="*":
            return (int(a)*int(b))
        elif operator=="**":
            return (int(a)**int(b))
    except ZeroDivisionError as e:
          return (e)# TODO: Handle division by zero
    except ValueError as v:
         return ("invalid input type")# TODO: Handle invalid numbers
    except TypeError as t:
        return (t) # TODO: Handle non-numeric input
    except Exception as e:
        return e # TODO: Handle any unexpected exceptions

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"