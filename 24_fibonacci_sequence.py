# Make a variable that says how many terms to print out.
terms = 25

# Create a sequence that will hold the terms.
sequence = [0, 1]

# Make a for loop that calculates and prints out the Fibonacci sequence for the specified number of terms.
for number in range(1, terms + 1):
    # Store n - 2 in a variable.
    nMinus2 = sequence.pop(len(sequence) - 2)
    sequence.insert(len(sequence) - 2, nMinus2)
    # Store n - 1 in a variable.
    nMinus1 = sequence.pop(len(sequence) - 1)
    sequence.append(nMinus1)
    # Add the number to the sequence.
    newNum = nMinus2 + nMinus1
    sequence.append(newNum)
# Take out the weird 0 that won't go away any other way that I've tried.
del sequence[terms - 1]
# Print it out.
print(sequence)