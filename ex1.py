numbers = []

for i in range(3):
    numbers.append(input('Digite o valor {}: '.format(i + 1)))

for number in numbers:
    print('Número {}: {}'.format(number, number))