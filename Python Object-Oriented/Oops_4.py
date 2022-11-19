class Cars:
    wheels = 4
    def __init__(self) -> None:
        self.color = "red"
        self.seats = 4

    def update(self):
        self.seats = 2
    
    def compare(self, other):
        if other.color == self.color and other.seats == self.seats:
            return True
        else:
            return False

    def config(self):
        return([self.color,self.seats])
    
RolsRoys = Cars()

Lamborghini = Cars()

RolsRoys.color = "Silver"
Lamborghini.update()
Lamborghini.color = "Yellow"

x,y = RolsRoys.config()
print(f"RolsRoys-> Color :{x} Seats: {y} Wheels {RolsRoys.wheels}")
a,b = Lamborghini.config()
print(f"Lamborghini-> Color :{a} Seats: {b} Wheels {Lamborghini.wheels}")

