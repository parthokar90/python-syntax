# Class and Object
# Class: A blueprint or template for creating objects (defined using the class keyword).

# Object: An instance of a class.

class Student:
    pass  # 'pass' is used to create an empty class

# Creating an object
student1 = Student()


# 2. Constructor (__init__) and self
# __init__(): The constructor method that runs automatically when a new object is created.

# self: Represents the instance of the class and binds the arguments to the attributes.

class Students:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

s1 = Students("Rahim", 20)
print(s1.name)  # Output: Rahim

# 3. Methods
# Functions defined inside a class that operate on the object's data are called methods.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

s1 = Student("Karim", 22)
print(s1.display_info())


# 4. Inheritance
# Allows a child class to inherit properties and methods from a parent class.

# Parent Class
class Animal:
    def eat(self):
        print("Eating...")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Barking...")

d = Dog()
d.eat()   # Inherited method (Output: Eating...)
d.bark()  # Child method     (Output: Barking...)

# 5. Encapsulation
# Restricts direct access to variables to prevent accidental modification.

# Public: self.name (Accessible everywhere)

# Protected: self._age (Single underscore — convention for internal use)

# Private: self.__balance (Double underscore — cannot be accessed directly from outside)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):  # Getter method
        return self.__balance

account = BankAccount(1000)
# print(account.__balance)  # Raises an AttributeError
print(account.get_balance()) # Output: 1000 

# 6. Polymorphism
# Allows different classes to use the same method name while performing different behaviors.

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Calling the same method name on different objects
animals = [Cat(), Dog()]
for animal in animals:
    animal.sound()


# 7. Abstraction
# Hides complex implementation details and exposes only the essential features using 
# Python's abc module.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement this method

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())  # Output: 16

