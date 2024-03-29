try:
    debt = float(input("Enter debt: "))
except ValueError:
    print("Incorrect value!")
    exit()

try:
    number_of_installments = int(input("How many installments do you want? (1, 3 or 5): "))

    if (number_of_installments == 1):
        total = debt
    elif (number_of_installments == 3):
        total = debt * 1.10
    elif (number_of_installments == 5):
        total = debt * 1.20
    else:
        print("Invalid option!")
        exit()
    
    installment = total / number_of_installments
except ValueError:
    print("Incorrect value!")
    exit()

print("\n***Result***")
print("Total: ${}".format(total))
print("Installment: ${}".format(installment))