'''Classes and Objects: The Blueprint and the Building
Class: Think of a class as a blueprint or a template. It defines what an object will be like  what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.'''


'''self Explained: Inside a class, self is like saying "this particular object." It's a way for the object to refer to itself. It's always the first parameter in a method definition, but Python handles it automatically when you call the method. You don't type self when calling the method; Python inserts it for you.
'''

'''Class vs. Instance Attributes:

Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.
Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.'''


class car :
    type = " 4 wheele type"

    def car_type(self):
        print(self)
        return "sports"
    def car_coloure(self):
        print(self)
        return "red"
    
c = car()
print(c.car_type())


d = car()
print(d.car_coloure())