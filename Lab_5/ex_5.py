# Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and Fish. 
# Add properties and methods to represent characteristics unique to each animal group.



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass 

    def move(self):
        pass 

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def make_sound(self):
        return "Mammal sound"

    def give_birth(self):
        return f"{self.name} is giving birth."

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return "Bird sound"

    def fly(self):
        return f"{self.name} is flying."

class Fish(Animal):
    def __init__(self, name, species, scale_color):
        super().__init__(name, species)
        self.scale_color = scale_color

    def make_sound(self):
        return "Fish sound"

    def swim(self):
        return f"{self.name} is swimming."



print("\n")
lion = Mammal(name="Leo", species="Lion", fur_color="Golden")
print(lion.make_sound())
print(lion.give_birth())

print("\n")
eagle = Bird(name="Eddie", species="Eagle", wingspan=2.5)
print(eagle.make_sound())
print(eagle.fly())

print("\n")
goldfish = Fish(name="Goldie", species="Goldfish", scale_color="Orange")
print(goldfish.make_sound())
print(goldfish.swim())
