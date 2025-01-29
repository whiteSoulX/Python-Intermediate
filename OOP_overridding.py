#parrent class
class Animal:
    def __init__(self,name):
        self.name=name

        def sound(self):
            print("Making Sound!")
#child class dog
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
            print("Woof!")


#child class cat

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
        print("Meow")


my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

my_dog.sound()
my_cat.sound()
