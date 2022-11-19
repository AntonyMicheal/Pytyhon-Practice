class Computer:
    def __init__(self, cpu, ram) -> None:
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Configuration is: "+self.cpu+" "+str(self.ram))


comp1 = Computer("i5",8)
comp1.config()
comp1 = Computer("Rayzen5",8)
comp1.config()