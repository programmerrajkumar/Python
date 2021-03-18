import random


class Person:
    address = ""
    noofpersons = 0 #static variable

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.__Id = random.randint(1, 100)  # private variable
        Person.noofpersons += 1

    def getName(self):
        return self.fname + self.lname

    def addAddress(self, address):
        self.address = address

    def printinfo(self):
        print(self.getName())
        print(self.age)
        print(self.address)

    def lifestyle(self):
        print("default life style")

    def getid(self):
        return self.__Id

    @staticmethod
    def displaypersoncount():
        print(Person.noofpersons)


class Employee(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)

    def greetings(self):
        print("Welcome", self.fname)

    def lifestyle(self):
        print("Employee lifestyle")
        print("from derived")
        Person.lifestyle(self) # or use super func

    class Salary:
        def __init__(self, salary):
            self.salary = salary

        def displaysalary(self):
            print(self.salary)


employee1 = Employee("raj", "", 18)
employee1.addAddress("1st street")
salary = employee1.Salary(100)
employee1.printinfo()
employee1.greetings()
salary.displaysalary()
del employee1.age  # deletes property from this object

print(employee1.getid())

Person.displaypersoncount()

print(employee1._Person__Id) #name mangling

employee1.lifestyle()