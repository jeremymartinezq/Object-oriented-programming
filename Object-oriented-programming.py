# Object Oriented Programming Example

class Emp():
    def __init__(self, ID, Name, Add):
        self.id = ID
        self.name = Name
        self.Add = Add

    class Freelance(emp):
        def __init__(self, ID, Name, Add):
            # Emp.__init__(self, ID, Name, Add)
            super().__init__(self, ID, Name, Add)
            self.Emails = Emails


# Driver Code
emp1 = Freelance(103, "John Marks", "FL", "jm@ucf.edu")
print(emp1.ID)
print(emp1.Name)
print(emp1.Add)
print(emp1.Emails)


# example
class Animals:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.Mammal = True

    def isMammal(self):
       if self.mammals:
           print("It is a mammal")

    def isDomestic(self):
        if self.domestic:
            print("It is domestic")

class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()

class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("It has a tail and legs")

# Driver Code:
Tom = Dogs()
Tom.isMammal()
obj2 = Dogs()
obj2.mammals = False
obj2.isMammal()
obj3 = Horses()
obj3.hasTailandLegs()


# super() with multi-level inheritence
# example
class Mammal():
    def __init__(self, name):
        print(name, "is a mammal")

class CanFly(Mammal)
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # calling parent class constructor
        super().__init__(canFly_name):


class CanSwim(Mammal)
    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        # calling parent class constructor
        super().__init__(canSwim_name):


# Driver Code
obj1 = CanSwim("Dog")

# Example
# define the class vehicle with name, color, price. A method called info()
# Its child class, Car, has same attributes. A method called info() that prints..
# and it has change_gear() that takes an integer, hwich is the gear number, and prints..


class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print("The Vehicle info:", self.name, self.color, self.price)


class Car(Vehicle):
    def change_gear(self, num):
        print(self.name, "changes the gear to", num)

    def info(self):
        print("The car info:", self.name, self.color, self.price)

class BodyType(Car):
   def __init__(self, name, color, price, body_type):
       super().__init__(name, color, price)



# ENCAPSULATION
# Access modifiers



class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):

        # call constructor of Base class
        Base.__init__(self)
        print("Calling protected member of Base class", self._a)

        # modify the protected variable
        self._a = 3
        print("Calling protected member of Base class", self._a)

# Driver Code:
obj1 = Derived()
obj2 = Base()
print("Accessing protected member of obj2", obj2._a)


# PRIVATE MEMBERS
#self.__name
class Base:
    def __init__(self):
        self.a = "printing a"
        self.__c = "printing c"




# Driver Code:
obj1 = Car("BMW M8", "Black", 100000)
obj1.info()

obj2.Vehicle("Lexus CS250", 30000)
obj2.info()

obj3 = Car("BMW x5", "Black", 50000, SUV)
obj3.info()







