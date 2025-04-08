# # Assignment 1: Design Your Own Class! 🏗️
# # Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# # Add attributes and methods to bring the class to life!
# # Use constructors to initialize each object with unique values.
# # Add an inheritance layer to explore polymorphism or encapsulation.
# # Activity 2: Polymorphism Challenge! 🎭

# # Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


# Activity 1 : Class
class Automobile:
    def __init__(self, name, wheels, icon): # Attributes
        self.name = name
        self.wheels = wheels
        self.icon = icon

    def no_of_wheels(self): # Methods
        return f"{self.name} has {self.wheels} number of wheels {self.icon}"
    
automobiles = [
    Automobile("BMX Bike", 2, "🏍"),
    Automobile("TVS", 3, "🛺"),
    Automobile("Ford", 4, "🚗"),
    Automobile("Tata", 6, "🚌"),
    Automobile("Volkswagen", 10, "🚛")]    

for automobile in automobiles:
    print(automobile.no_of_wheels())




# Activity 2 : TO EXPLAIN POLYMORPHISM

#Base Class
class Automobile:
    def __init__(self, name):
        self.name = name

    def speed(self):
        return f"{self.name} moves at {self.speed} km/hr"

#Sub-Classes
class Bike(Automobile):
    def speed(self):
        return f"{self.name} moves at 20 km/hr"

class Tricycle(Automobile):
    def speed(self):
        return f"{self.name} moves at 35 km/hr"

class Car(Automobile):
    def speed(self):
        return f"{self.name} moves at 50 km/hr"
    
class Van(Automobile):
    def speed(self):
        return f"{self.name} moves at 45 km/hr"
    
class Truck(Automobile):
    def speed(self):
        return f"{self.name} moves at 40 km/hr"
    
automobiles = [
    Bike("BMX Bike"),
    Tricycle("TVS"),
    Car("Ford"),
    Van("Tata"),
    Truck("Volkswagen")]    

for automobile in automobiles:
    print(automobile.speed())















