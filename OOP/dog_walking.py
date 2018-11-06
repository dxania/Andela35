class Pet:
    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    group = 'mammals'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def walk(self):
        return f"{self.name} is walking"

the_dogs = Pet([
    Dog("Tom", 6),
    Dog("Fletcher", 7),
    Dog("Larry", 9)
])

the_dogs.walk()