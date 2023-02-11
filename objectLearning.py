#objectLearning.py

'''
Title: Object learning
Author: Jason Wang
Date-Created: 2023-02-11
'''
class car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


class dog: 
    #Class attribute - same for every class
    Species = "Dog, mhm sure is a dog"

    def __init__(self, name, age): 
        #first parameter is always "self" The __init__ makes is setting the default instances for parameters
        self.name = name
        self.age = age
        print("initialized")

    #instance method (this is like a function defined within a class)
    def description(self):
        print(f"{self.name} is {self.age} years old")

    #Another instance method
    def speak(self, sound):
        print(f"{self.name} barks {sound}")

    def __str__(self): #This defines what it will do when you print this class
        return f"{self.name} is {self.age} years old"

    #this class now has two instance methods that can be called upon


#Child classes the PARENT class goes into the parenthesis of the CHILD class
# NOTE: changes to the parent class will automatically also affect child classes 


class ShibaInu(dog):
    #to overide a method defined on parent class you must define with the same name on child class
    def speak(self, sound="much woof"):
        print(f"{self.name} says {sound}")

class Husky(dog):
    #you can access the parent class from inside a method of a child class with super()
    def speak(self, sound="arf"):
        print(super().speak(sound))
        #this is calling or a speak() method from the parent (dog) and using the variable "sound"  
        # super wont always just search parent it will search entire hirearchy 


#python automatically removes the "self" parameter only needs to input "name" and "age"
a = dog("Doge", 4)
b = dog("Miles", 5)

a.description()
a.speak("woof")
print(a)

a2 = ShibaInu("Doge2", 8)
b2 = Husky("Miles2", 10)
a2.speak()
b2.speak()
a2.description()
print(type(a), type(a2))
print(isinstance(a2, dog)) #this one takes two arguments the OBJECT and the CLASS 
print(isinstance(a2, Husky))
print(isinstance(a2, ShibaInu))


## Check understanding

'''
carA = car("blue", "20000")
carB = car("red", "30000")
print(carA)
print(carB)
'''

