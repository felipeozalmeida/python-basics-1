# Initialize variables
numbers = []
average = 0.0

# Get values
for i in range(3):
    numbers.append(float(input("Enter value {}: ".format(i + 1))))

# Sum up everything
for number in numbers:
    average += number

# Get average
average /= len(numbers)

# Show average
print("Average: {}".format(average))
