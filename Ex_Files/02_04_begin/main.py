# Define lists of Beatles' names and their ages
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

# Print each name with its corresponding age using a while loop
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

# Print each name using a for loop
for name in NAMES:
    print(name)

# Print each name with its corresponding age using zip in a for loop
# zip pairs up elements from NAMES and AGES, so each iteration gives a name and its corresponding age
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# Print each name in reverse order
for name in reversed(NAMES):
    print(name)

# Print numbers from 0 to 4 using range in a for loop
for i in range(5):
    print(i)

# enumerate (placeholder for future code)
