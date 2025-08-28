from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        """Initialize the animal with a name."""
        self.name = name

    @abstractmethod
    def move(self):
        """Abstract method for movement - must be implemented by subclasses."""
        pass

    def speak(self):
        """Generic animal sound."""
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def move(self):
        """Dog moves by running."""
        print(f"{self.name} is running! 🐕")

    def speak(self):
        """Dog barks."""
        print(f"{self.name} says: Woof! Woof!")

class Bird(Animal):
    def move(self):
        """Bird moves by flying."""
        print(f"{self.name} is flying! 🐦")

    def speak(self):
        """Bird chirps."""
        print(f"{self.name} says: Tweet! Tweet!")

class Fish(Animal):
    def move(self):
        """Fish moves by swimming."""
        print(f"{self.name} is swimming! 🐟")

    def speak(self):
        """Fish makes bubble sounds."""
        print(f"{self.name} says: Blub! Blub!")

class Snake(Animal):
    def move(self):
        """Snake moves by slithering."""
        print(f"{self.name} is slithering! 🐍")

    def speak(self):
        """Snake hisses."""
        print(f"{self.name} says: Hiss! Hiss!")
