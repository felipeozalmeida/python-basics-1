class Worker:
    name = ""
    salary = 0.0

    def __init__(self, name="John", salary=1000):
        self.name = name
        self.salary = salary

    def raise_salary(self, percent=10.0):
        self.salary = self.salary * (1 + percent / 100)


print("\n***Create Worker***")
name = input("Insert name: ")
salary = float(input("Insert salary: "))
worker = Worker(name, salary)

print("\n***Raise salary***")
if (input("Do you want to raise salary? [Y/n] ").upper() == "Y"):
    new_salary = float(input("Enter desired increase in percentage (i.e. 10): "))
    print("\n***Raising salary by {}%***".format(new_salary))
    worker.raise_salary(new_salary)

print("\n***Worker***")
print("Name: {}".format(worker.name))
print("Salary: {}".format(worker.salary))
