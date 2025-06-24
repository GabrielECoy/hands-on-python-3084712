# Define a list of Beatles' names
NAMES = ["John", "Paul", "George", "Ringo"]
# Define a list of their ages
AGES = [20, 21, 22, 23]

# Assign the first name to JOHN
JOHN = NAMES[0]
# Assign the second name to PAUL
PAUL = NAMES[1]

# Slice: first two names
JOHN_PAUL = NAMES[:2]
# Slice: last two names
GEORGE_RINGO = NAMES[2:]
# Reverse the list of names
REVERSE = NAMES[::-1]
# Get every other name from the list
EVERY_OTHER = NAMES[::2]

# Print the sum of ages
print(sum(AGES))
# Print the minimum age
print(min(AGES))
# Print the maximum age
print(max(AGES))

# Print the first two names
print(JOHN_PAUL)
# Print the last two names
print(GEORGE_RINGO)
# Print the names in reverse order
print(REVERSE)
# Print every other name
print(EVERY_OTHER)
# Print the alphabetically last name
print(max(NAMES))
# Print the alphabetically first name from every other name
print(min(EVERY_OTHER))