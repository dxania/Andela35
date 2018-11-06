class Pet:
    def __init__(self, dogs):
        self.dogs = dogs

class Dog:
    group = 'mammals'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False

the_dogs = Pet([
    Dog("Tom", 6),
    Dog("Fletcher", 7),
    Dog("Larry", 9)
])

print(f"I have {len(the_dogs.dogs)} dogs")
    
for pet in the_dogs.dogs:
    print(f"{pet.name} is {pet.age}")
    
pet.eat()

if pet.is_hungry:
    print("My dogs are hungry")
else:
    print("My dogs are not hungry")

print(f"They are all {Dog.group}, of course")
