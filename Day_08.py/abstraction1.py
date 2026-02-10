# # Syntax
# from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def abs_method(self):
#         pass

#     #concrete method
#     def concrete_method(self):
#         #implementation

# class B(A):
#     def abs_method(self):
#         #implementation


from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    def conc(self):
        print("I am a concrete method")

class B(A):
    def method1(self):
        print("I am in classB")
    
    def method2(self):
        print("Method 2")

obj=B()
obj.method1()
obj.conc()

print("----------------------------------")

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def brakes(self):
        print("The brakes are applied.")

class Car(Vehicle):
    def start_engine(self):
        print("The car Engine is started")

class Bike(Vehicle):
    def start_engine(self):
        print("The bike Engine is started")

class Bus(Vehicle):
    def start_engine(self):
        print("The Bus Engine is started")

c=Car()
c.start_engine()
c.brakes()


