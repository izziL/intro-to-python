# This will return the ticket price for every specified buyer age and isTuesday boolean.
def ticketCalculator(buyerAge, isTuesday):
    # If it is Tuesday, the person gets a $2 discount.
    if isTuesday == True and buyerAge < 13:
        return 6
    elif isTuesday == True and buyerAge > 65:
        return 8
    elif isTuesday == True and buyerAge >=13 and buyerAge <= 65:
        return 10
    # Otherwise, the person pays regular price.
    elif isTuesday == False and buyerAge < 13:
        return 8
    elif isTuesday == False and buyerAge > 65:
        return 10
    else:
        return 12

# Run the program for the inputs.
testAges = [13, 34, 88, 45]
for age in testAges:
    # I was bored so I figured out how to randomize the boolean.
    import random
    isTuesday = random.choice([0, 1])
    if isTuesday == 0:
        isTuesday == False
    else:
        isTuesday == True
    # Print the statement, saying what the person's age is, whether it is discount Tuesday, and their final ticket price.
    print("You are " + str(age) + " years old. Since it", end = " ")
    if isTuesday == True:
        print("is", end = " ")
    else:
        print("isn't", end = " ")
    print("discount Tuesday, your ticket will cost you $" + str(ticketCalculator(age, isTuesday)) + ".")
