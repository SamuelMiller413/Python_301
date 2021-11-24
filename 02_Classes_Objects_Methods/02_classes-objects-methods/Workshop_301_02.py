# >>>>>>>>>>>>>  2) Classes, Objects, and Methods / Introduction To Object-Oriented Programming


# Introduction to Object-Oriented Programming

# so far I've used Python mainly as 
#     Procedural Programming Language,
# however there are more 
#     Programming Paradigms.

# This Module will be about Object-Oriented Programming

# Object-Oriented Programming, often abbreviated as OOP, is a programming paradigm that is commonly used across many programming languages.

# >>>>>>>>>>>>>  OOP From Space_

# Follow along.
# Talking about 'classes

# '''
# Create a Planet class that models attributes and Methods of 
# a planet object

# se the appropriate dunder method to get informative output with print()
# '''

# class Planet():

#     def __init__(self, name, color, system):                  # these double Underscores are a method
#                                                             # called a 'dunder method'
#         self.name = name
#         self.color = color
#         self.system = system
#     def __str__(self):
#         return f"Planet {self.name} is a {self.color} planet in the {self.system}."

#     def bears_life(self):
#         if self.color.lower() == 'blue':
#             return True
#         else:
#             return False

# mars = Planet('Mars', 'red', 'Solar System')
# earth = Planet('Earth', 'blue', 'Solar System')
# naboo = Planet('Naboo', 'blue', 'Naboo System')

# print(mars)
# print(earth)
# print(naboo)
# print(mars.bears_life())
# print(earth.bears_life()) 

# print(mars.name, mars.color, mars.system)



# >>>>>>>>>>>>>  Programming Paradigms


# Programming Paradigms:

    # Object-oriented programming is a programming paradigm 
    # that organizes code around objects rather than actions 
    # and data rather than logic.

#   - Code-centric organization asks what's happening 
#   and focuses on how the code acts on your data. 
#   It's the type of approach used for procedural 
#   and functional programming.

#   - Data-centric organization asks what's being affected 
#   and focuses on how the data controls the access to your code. 
#   This is the approach used in OOP.




# >>>>>>>>>>>>>  Main OOP Concepts


# Main OOP Concepts:
    # The four primary traits of OOP are:

        # Abstraction
        # Encapsulation
        # Inheritance
        # Polymorphism


# Abstraction:
# When you apply abstraction, you reduce information to the essential concepts.

    # In the context of OOP, abstraction means that you create a black box when writing your code. 
    # This means that your users won't need to know 
    # about all the contents and capacities of your implementation, 
    # but they'll still be able to use it.

    # Python's basic unit of abstraction is the 'class.'
        # A class defines the form of an object by specifying both 
        # the data and 
        # the code that operates on the data.


# Encapsulation:
# Encapsulation means that you're binding your data and the code that changes it together.

    # 'Public Interface' that exposes the data that you want to be accesed and worked with.
    # 'Private interface' that indicates data and methods that shouldn't be modified by the user.

# When code and data are linked together like this, you can speak of an object.


# Inheritance:
# Inheritance allows one object to access the properties of its parent object.
    
    # If you define a class that inherits from another class, 
    # then an object of the child class will be everything that the parent class is, 
    # and can do everything that the parent class can do.

    # For example:
        # For example: 
        # you can think of an apple as being classified as an "Apple" object. 
        # Apples are fruits, so it could inherit from a "Fruit" class. 
        # If all fruits in your Fruit class are defined as "a product of plant growth", 
        # then your Apple that inherits from Fruit, 
        # would automatically also be "a product of plant growth".
            # If you define that every Fruit is edible, 
            # then each Apple that inherits from Fruit 
            # will be edible as well.


# Polymorphism:
# The term polymorphism stands for "having many forms". 
# In OOP, polymorphism means that objects that belong to different classes 
# can respond to the same message, however, they can respond in different ways.

    # For Example:
    # You could have two objects, 'Dog' and 'Cat',
    # that both inherit from an 'Animal' class. 
    # They can both have a method .greet() that was
    # initially defined in the parent class. 
    # Both dogs and cats can greet others, 
    # but they do it in distinctly different ways. 
    # Therefore, calling .greet() on a Dog object 
    # will have a different effect than calling .greet() on a Cat object.

        # You could model this in OOP by defining
        #  an empty .greet() method in your Animal class, 
        # and overwriting the method with 
        # different functionality in both the Dog and the Cat class.

# The object-oriented programming paradigm builds on top of four fundamental concepts:

# 1. Abstraction creates a black box that shows only what's necessary in a user-friendly interface.
# 2. Encapsulation binds data and logic together, exposing a public interface and hiding other parts in a private interface.
# 3. Inheritance allows classes to pass on their attributes and methods to child classes.
# 4. Polymorphism gives the possibility for different classes to implement the same attributes and methods, but handle their logic differently.



# >>>>>>>>>>>>>  Cooking With Python


# ingredients = ['carrot', 'pea', 'squash']


# ingredients = {
#                 'carrots': {'name': 'carrot', 'amount': 3},
#                 'peas': {'name': 'pea', 'amount': 12}
#               }

# print(f"Let's take {ingredients['carrots']['amount']} of {ingredients['carrots']['name']} and {ingredients['peas']['amount']} of {ingredients['peas']['name']}.")



# >>>>>>>>>>>>>  Your Own Custom Data Types_


# Use Classes to make your own data types.



# >>>>>>>>>>>>>  Custom Python Objects


# Custom Python Objects:

# A class is a blueprint for an object.
# A class defines what an object instance of that class will look like.


# What is an object?

# Everything in Python is an object. str, int, list, dict, function.
    # All are objectss.


# Custom Objects:
# 
# class Ingredient:
#     """creates an empty Ingredient object."""
#     pass

# i = Ingredient()  # Instantiating an object of the class.
# print(type(i))  # OUTPUT: <class '__main__.Ingredient'>

# User defined types are call 'classes'



# >>>>>>>>>>>>>  Defining And Instantiating a Class


# Defining a Class:

# Similar to a Python function, you define a class with a specific 'keyword'. 
#   while you use def for a function, you use class for a class:

        # class ClassName:
        #     """docstring"""
        #     pass

# After the class keyword follows the name of your class, usually in singular.
# Classes in Python are named following the CapCase convention.

# docstrings are recommended in order to help other developers to work with your classes. 


# Instantiating a Class:

# You'll use a class' info to 
    # 'instantiate' an object.
        # also called an 'instance of that class. 

# use the same syntax as when calling a function:
# i = iungredient()
    # this line of code 'instantiates' an Ingredient object and saves it to the variable, 'i'

    # d = dict()
    #     this above line instantiates an empty dict object.


# Recap:
# A class definition in Python consists of:

# the class keyword
# the name of your class in CapCase and singular
# a colon (:)
# the docstring of the class, indented by four spaces
# the body of your class definition containing all the code that makes up your class. This code also needs to be indented by four spaces.



# >>>>>>>>>>>>>  An Empty Class_


# --> see ingredients.py



# >>>>>>>>>>>>>  Instance Variables


# class Ingredient:
#     """Creates an empty Ingredient object."""
#     pass

# i = Ingredient()

# i.name = "carrot"       # Instance Variable
# print(i.name)  # OUTPUT: carrot

# print(name)     # OUTPUT: NameError: name 'name' is not defined 
    # You could have a variable 'name' 
    # in the global scope of your script, 
    # and it won't interfere with i.name.


# The Constructor Method:

# While it's possible to assign instance variables 
# in the way you just did, this is rare in practice. 
# Instead, you want to use your class as a blueprint that 
# defines what variables each instance should have.

# The blueprint for your 'class constructor '
# is Python's dunder init
# (__init__()) method.

# This method gets called when you're creating a new instance. 
# Any attributes you define here will apply for 
# all instances of the class you'll create:

# class Ingredient:
#     """Models an Ingredient. Currently only carrots!"""

#     def __init__(self):
#         self.name = "carrot"

# i = Ingredient()
# print(i.name)  # OUTPUT: carrot

# t'll likely remind you of a function definition. 
# Indeed, you can think of methods as: 
        # functions that belong to an object.

# c = Ingredient()
# print(c.name) # OUTPUT: carrot


# class Ingredient:
#     """Models a food item used as an ingredient."""

#     def __init__(self, name, size, taste):
#         self.name = name
#         self.size = size
#         self.taste = taste


# i = Ingredient("peas", "little", "buttery")
# c = Ingredient("cauliflower", "big", "salty")
# b = Ingredient("broccoli", "big", "salty")
# d = Ingredient("dandelion", "little", "earthy")

# print(i.name, c.name, b.name, d.name)
# print(i.name, i.size, i.taste)

# def __str__(self):
# #         return f"Planet {self.name} is a {self.color} planet in the {self.system}."



# >>>>>>>>>>>>>  Methods


# Methods:
# Similar to how you can think of attributes as instance variables, 
# you can think of methods as instance functions.

# Info: Dunder init, and other dunder methods that 
    # you'll get to know in the next lesson, 
    # are sometimes called special methods or magic methods. 
    # There's nothing special or magical about them, 
    # as you'll see in this lesson. 
    # The only difference to a "normal" method is that 
    # they aren't meant to be called explicitly.

# Adding an 'expire()' method to your ingredient class:
# class Ingredient:

#     """Models a food item used as an ingredient."""
#     def __init__(self, name):
#         self.name = name

#     def expire(self):
#         """Expires the ingredient."""
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name

# i = Ingredient("peas")
# print(i.name)  # OUTPUT: peas
# i.expire()
# print(i.name)  # OUTPUT: expired peas
# print(i.name)  # OUTPUT: expired peas



# >>>>>>>>>>>>>  Doing Something with your Objects_



# ---> see ingredients.py

# from ingredients import Ingredient

# carrots = Ingredient("carrots", 3)



# >>>>>>>>>>>>>  The self Parameter


# The Self Parameter:
#     Connected Awareness:
#         Python Class instances are 'self'-aware! 
#         When you reference self within a class definition, 
#         it means that you're referencing the 
#         'instance object tself'
        # That means, for example, that the reference self.name 
        # will be accessible inside of every method that takes 
        # self as its first parameter:

# class Ingredient:

#     """Models a food item used as an ingredient."""
#     def __init__(self, name):
#         self.name = name

#     def expire(self):
#         """Expires the ingredient."""
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name
#  - __init__() can assign the value of name that it receives 
#  during instantiation to the object through self.name = name.


#  - expire() can access and change the value of self.name 
#  with the references to it in its method body.

# In your class definition, you wrote that expire() takes exactly one argument, self. However, in the code snippet above you seemingly call expire() without any arguments. The reason for this is that you're passing the reference to your object instance, i, by calling the method on it.

# When you compare this to a function, you can think that i.expire() is equivalent to expire(i), where i points to your Ingredient() object that inside of your class definition gets referenced through self.

# What's the difference between functions and methods?

# A short rule-of-thumb answer to this question is that 
# methods are functions that are part of a class.



# >>>>>>>>>>>>>  Dunder Methods


# Common Dunder Methods

#   __init__() for constructing instances
#   __str__() for user-focused documentation
#   __repr__() for developer-focused documentation
#   __add__() for adding instances with the + operator

# __init__() is the constructor method for your class. 
#     It's used to initialize a class instance either with 
#     default values or with arguments that you passed 
#     when instantiating a new object.



# >>>>>>>>>>>>>  Dunder Methods for Representation

# __str__() and __repr__()


# readability:

# __str__() helps yopu create user-friendly output that describes your object when calling print() or str() on it. 
    # you can think of it as being aimed at an end-user.

# example:
    # def __str__(self):
    #     return f"{self.name} ({self.amount})"

    # c = Ingredient("carrot", 5)
    # print(c)  # OUTPUT: carrot (5)

# When you don't implement the __str__() method, 
# Python will fall back to the output of __repr__() 
# when print() is called on a custom object.


# Documentation: __repr__():

# example:
# def __repr__(self):
#     return f"Ingredient(name={self.name}, amount={self.amount})"

# This output should be very clear and concise, 
# but can often turn out to be less user-friendly than __str__(). 
# You can think of it as being aimed at developers 
# and should help them to debug potential issues:

# c = Ingredient("carrot", 5)
# print(c)  # OUTPUT: carrot (5)
# print(repr(c))  # OUTPUT: Ingredient(name=carrot, amount=5)


# Recap:

# Using __repr__() and __str__() makes understanding and 
# debugging your custom classes more user-friendly. 
# If you end up implementing only one of the two, 
# make sure that it's __repr__().



# >>>>>>>>>>>>>   Implementing Operators:


# In this lesson, you'll learn how you can implement __add__() 
# so that you can add two instances of your 
# Ingredient() class together using the familiar + operator.


# You can implement __add__() as well for your custom functions, which gives them access to use the intuitive + operator to work with two instances. Of course, you'll need to decide what it means for your object to add two instances together.

# For example, you could decide that adding two Ingredient() objects would mash together their names and create a single new Ingredient() item from the two inputs:

# class Ingredient:

#     """Models a food item used as an ingredient."""
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount

#     def expire(self):
#         """Expires the ingredient."""
#         print(f"whoops, these {self.name} went bad...")
#         self.name = "expired " + self.name

#     def __str__(self):
#         return f"{self.name} ({self.amount})"

#     def use(self, use_amount):
#         self.amount -= use_amount

#     def __add__(self, other):
#         """Combines two ingredients."""
#         new_name = self.name + other.name
#         return Ingredient(name=new_name, amount=1)

# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)

# # s = c.__add__(p)
# # print(s)  # OUTPUT: carrotpea (1)

# # -or-

# s = c + p
# print(s)  # OUTPUT: carrotpea (1)

