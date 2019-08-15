class Worker:
    name = ""
    salary = 0.0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def raiseSalary(self):
        self.salary *= 1.10

print("\n***Create Worker***")
name = input("Insert name: ")
salary = float(input("Insert salary: "))
john = Worker(name, salary)

print("\n***Raising salary by 10%***")
john.raiseSalary()

print('\n***Worker***')
print('Name: {}'.format(john.name))
print('Salary: {}'.format(john.salary))