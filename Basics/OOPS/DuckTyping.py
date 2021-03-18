class Duck:
    def quack(self):
        print("Duck,Quack quack..")

    def fly(self):
        print("Duck,Fly")

# Duck typing is for Dependency injection

class Human:
    def quack(self):
        print("Human,Quack quack..")

    def fly(self):
        print("Human,Fly")

class Test:
    def invoke(self,animal):
        animal.quack()
        animal.fly()

test=Test()
test.invoke(Duck())
test.invoke(Human())