class Person:
    def __init__(self) -> None:
        self.name = "Navin"
        self.age = 20

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
    

p1 = Person()
p2 = Person()

p1.age = 50

if p1.compare(p2):
    print("They are the same")
else:
    print("They are different")
# Self keeps track of which object have which values