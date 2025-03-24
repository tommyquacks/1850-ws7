class VirtualPet:
    """
    A class representing a virtual pet with a name, energy, and hunger level.
    """
    def __init__(self, name):
        """
        Initializes the pet with a name, and default values for energy and hunger.
        """
        self.name = name
        self.energy = 10
        self.hunger = 0

    def play(self):
        """
        Simulates playing:
        - Reduces energy by 2
        - Increases hunger by 2
        - If energy is too low, it refuses to play
        """
        if self.energy >= 2:
            self.energy -= 2
            self.hunger += 2
        else:
            print("Too tired to play")

    def feed(self):
        """
        Feeds the pet by reducing hunger.
        Overfeeding is allowed but hunger can't go below 0.
        """
        self.hunger = max(0, self.hunger - 3)

    def sleep(self):
        """
        Simulates sleeping, which restores energy.
        """
        self.energy += 10

    def __str__(self):
        """
        Returns a string with the pet's status.
        """
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"
