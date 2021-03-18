class Programmer:

    def __init__(self):
        self._name = ""
        self._age = 0

    def set_name(self, n):
        print("name setter")
        self._name = n

    def get_name(self):
        print("name getter")
        return self._name

    def delete_name(self):
        del self._name

    @property
    def age(self):
        print("age getter")
        return self._age

    @age.setter
    def age(self, a):
        print("age setter")
        if a < 18:
            raise ValueError("Age should be greater than 18")
        self._age = a

    name = property(get_name, set_name, delete_name)


p1 = Programmer()
p1.name = "raj"
print(p1.name)

p1.age = 18
