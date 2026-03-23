class Animal():
    def __init__(self):
        self.name=""
    
    def legs(self):
        print("I have 4 legs!")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def dog_name(self):
        self.name=input("Enter the name of the dog: ")
        print(f"The dog's name is {self.name}")

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def cat_name(self):
        self.name=input("Enter the name of the cat: ")
        print(f"The cat's name is {self.name}")

animal1=Dog()
animal1.dog_name()
animal1.legs()

animal2=Cat()
animal2.cat_name()
animal2.legs()