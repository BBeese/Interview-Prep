class Animal():
    numAnimals = 0
    def __init__(self):
        Animal.numAnimals += 1
        self.isAnimal = "I am an animal"

    def roar(self):
        return ("This animals roar has not yet been configured.")

class Dolphin(Animal):
    def __init__(self):
        super().__init__()
        self.numLegs = 0
        self.numFins = 4 # right?

    def roar(self):
        return "EEEEE"

class Turtle(Animal):
    def __init__(self):
        super().__init__()
        self.numLegs = 4
        self.numFins = 0

def main():
    print("Number of animals before object is instantiated:", Animal.numAnimals)
    dolphin = Dolphin()
    print("Number of animals after object is instantiated:", Animal.numAnimals)
    turtle = Turtle()
    print(turtle.roar())

main()