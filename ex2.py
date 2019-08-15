class Worker:
    name = ""
    salary = 0.0

    def __init__(self, name="John", salary=1000):
        self.name = name
        self.salary = salary

    def raiseSalary(self):
        self.salary *= 1.10


print("\n***Create Worker***")
name = input("Insert name: ")
salary = float(input("Insert salary: "))
worker = Worker(name, salary)

print("\n***Raising salary by 10%***")
worker.raiseSalary()

print("\n***Worker***")
print("Name: {}".format(worker.name))
print("Salary: {}".format(worker.salary))
