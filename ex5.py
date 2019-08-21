print("\n***Create student***")
name = input("Insert your name: ")
grades = []
average = 0

for i in range(3):
    try:
        grades.append(float(input("Insert grade no. {}: ".format(i + 1))))
    except ValueError:
        print("Incorrect value!")
        exit()

for grade in grades:
    average += grade

average /= len(grades)

status = "Approved" if average >= 8 else "Disapproved"

print("\n***Student info***")
print("Name: {}".format(name))
print("Avg.: {}".format(average))
print("Status: {}".format(status))