class Computer:
    def __init__(self) -> None: # gets executed the moment the object is created
        print("in init")
    def spec(self):
        print("i5, 8 GB, 1TB")

com1 = Computer() # Object 1
com2 = Computer() # Object 2

Computer.spec(com1)
Computer.spec(com2)

# or

com1.spec()
com2.spec()