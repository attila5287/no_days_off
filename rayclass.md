'''
Circuitous, LLC -
An Advanced Circle Analytics Company

Summary: Toolset for New-Style Classes

1. Inherit from object.
2. Instance variables for information unique to an instance.
3. Class variables for data shared among all instances.
4. Regular methods need "self" to operate on instance data.
5. Class methods implement alternative constructors. They need "cls"
   so they can create subclass instances as well.
6. Static methods attach functions to class. They don't need
   either "self" or "cls".
   Static methods improve discoverability and require context to be specified.
7. A property() lets getter and setter methods be invoked automatically by
   attribute access. This allows Python classes to freely expose their
   instance variables.
8. The "__slots__" variable implements the Flyweight Design Pattern by
   suppressing instance dictionaries
9. The __method() is a class local reference, making sure the method refers
   to this class's method, not its childrens'.
'''

import math


class Circle(object):  # new-style class
    'An advanced circle analytic toolkit'

    # flyweight design pattern suppresses
    # the instance dictionary

    __slots__ = ['diameter']
    version = '1.0'  # class variable

    def __init__(self, radius):
        # init is not a constructor. It's job is to initialize the instance variables

        self.radius = radius  # instance variables

    @property  # convert dotted access to method calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):  # regular methods have 'self' as first argument
        'Perform quadrature on a shape of uniform radius'
        p = self.__perimeter()  # class local reference
        r = p / math.pi / 2.0
        return math.pi * r**2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod  # alternative constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod  # attach functions to classes
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


class Tire(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25
