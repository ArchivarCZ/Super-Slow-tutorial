class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def get_older(self, years):
        self.age += years

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", Salary: {self.salary}"
        return text
        # return f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Salary{self.salary}"

    def calculate_yearly_salary(self):
        return self.salary * 12



person1 = Person("Mike", 25, 178)
person2 = Person("Sara", 23, 168)
worker1 = Worker("Henry", 40, 176, 3000)

print(worker1)
print(worker1.calculate_yearly_salary())