class user:
    noofusers = 0  # static variable

    def __init__(self, name):
        user.noofusers += 1
        self.name = name




a = user("raj")
b = user("kumar")
b.noofusers += 1
user.displayusercount()
a.displayusercount()
b.displayusercount()
print(b.noofusers)