numbers = []
result = 0.0

print("\n***Get values***")

for i in range(2):
    try:
        numbers.append(float(input("Insert floating point value no. {}: ".format(i + 1))))
    except ValueError:
        print("Invalid value!")
        exit()

option = input("Choose an option [1, 2, 3]: ")

if (option == "1"):
    result = numbers[0] + numbers[1]
elif (option == "2"):
    result = numbers[0] * numbers[1]
elif (option == "3"):
    result = numbers[0] / numbers[1]
else:
    print("Invalid option!")
    exit()

print("\n***Calc results***")
print("Value: {}".format(result))