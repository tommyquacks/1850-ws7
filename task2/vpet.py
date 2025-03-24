class VirtualPet:
  
    def __init__(self, name):
       
        self.name = name
        self.energy = 10
        self.hunger = 0

    def play(self):
       
        if self.energy >= 2:
            self.energy -= 2
            self.hunger += 2
        else:
            print("Too tired to play")

    def feed(self):
      
        self.hunger = max(0, self.hunger - 3)

    def sleep(self):
       
        self.energy += 10

    def __str__(self):
       
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"
