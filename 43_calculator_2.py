# This cleans the input.
def clean(x):
    return x.lower().strip()

# The following functions will add, subtract, multiply, and divide. There is error protection.
def add(a, b):
    try:
        addition = a + b
        return "The sum of " + str(a) + " and " + str(b) + " is " + str(addition) + "."
    except:
        return "There is an error, but I'm having trouble determining it."

def subtract(a, b):
    try:
        difference = a - b
        return "The difference of " + str(a) + " and " + str(b) + " is " + str(difference) + "."
    except:
        return "There is an error, but I'm having trouble determining it."

def multiply(a, b):
    try:
        product = a * b
        return "The product of " + str(a) + " and " + str(b) + " is " + str(product) + "."
    except:
        return "There is an error, but I'm having trouble determining it."

def divide(a, b):
    try:
        quotient = a / b
        return "The quotient of " + str(a) + " and " + str(b) + " is " + str(quotient) + "."
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except:
        return "There is an error, but I'm having trouble determining it."

# This is our calculator function.
def calculator():
    # Ask for and clean the operator.
    operator = input("Would you like to add, subtract, multiply, or divide? Please type out the whole word.")
    operator = clean(operator)

    # Ask for the two numbers. If it is a value error, the computer will tell the user to enter all numbers.
    if operator == "add" or operator == "subtract" or operator == "multiply" or operator == "divide":
        try:
            num1 = float(input("What is the first number you would like to " + operator + "?"))
            num2 = float(input("What is the second number you would like to " + operator + "?"))
        except ValueError:
            return "Please enter all numbers, not a mix of letters and numbers."
    else:
        print("Sorry, I don't understand which operation you want to do. Please try again.")
        return calculator()

    # Calculate.
    if operator == "add":
        return add(num1, num2)
    elif operator == "subtract":
        return subtract(num1, num2)
    elif operator == "multiply":
        return multiply(num1, num2)
    elif operator == "divide":
        return divide(num1, num2)
        
# Run the function.
print(calculator())