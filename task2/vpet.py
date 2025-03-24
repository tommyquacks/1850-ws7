class VirtualPet:
  
    def __init__(self, name):
        """
        Initializes the pet with a name, hunger, and happiness level.
        """
        self.name = name
        self.hunger = 50  # 0 = full, 100 = starving
        self.happiness = 50  # 0 = sad, 100 = super happy

    def feed(self):
        """
        Decreases the pet's hunger level.
        """
        self.hunger = max(0, self.hunger - 10)

    def play(self):
        """
        Increases the pet's happiness level.
        """
        self.happiness = min(100, self.happiness + 10)
        self.hunger = min(100, self.hunger + 5)  

    def get_status(self):
        """
        Returns a summary of the pet's status.
        """
        return f"{self.name}: Hunger={self.hunger}, Happiness={self.happiness}"
