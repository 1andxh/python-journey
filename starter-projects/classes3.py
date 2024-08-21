class Dog:
    dogs = []



    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("woof!")

class German(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def how_old(self):
       print(Dog, "is 3 yeras old") 

    

# tim = Dog("tim")
# jim =  Dog("Jim")
# print(Dog.num_dogs())
# print(Dog.dogs)
            
Dog.bark(5)
German.how_old(Dog)

