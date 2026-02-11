#Task 1: __str__ and __repr__ (Difference Task)
class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return "I am the class Book!"

    def __repr__(self):
        return f"Book {self.title} author's name is {self.author} and it's price is {self.price}." 

obj=Book("Advanced Python", "Charlie", 450)
obj1=Book("Basic python", "Jhon", 300)
print(obj)
print(obj1)
print([obj, obj1])

print("---------------------------------------")

#Task 2: __eq__ (Equality Checking Task)
class Mobile:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False
        
        
m1 = Mobile("Samsung", "GalaxyM1", 5000)
m2 = Mobile("Apple", "Orange", 150000)
m3 = Mobile("Samsung", "GalaxyM11", 10000)

print(m1 == m2)
print(m1 == m3)
print(m2 == m3)

print("---------------------------------------")


#Task 3: __new__ and __init__ (Object Creation Flow Task)
class User:
    def __new__(cls, *args, **kwargs):
        print("Object is being created")
        return super().__new__(cls) 
    
    def __init__(self, name):
        self.name = name
        print("Object is initialized")

u1 = User("Arpita")

print("---------------------------------------")

#Task 4: __enter__ and __exit__ (Context Manager Task)
class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")

with DatabaseConnection():
    print("Performing Query...")

print("---------------------------------------")
#Task 5: __call__ (Callable Object Task)
class Calculator:
    def __call__(self, a, b):
        return a+b
obj = Calculator()
print(obj(10, 20))
print("---------------------------------------")


#Task 6: __getitem__ and __setitem__ (Indexing Task)
class ShoppingCart:
    def __init__(self, items):
        self.items = items   

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

cart = ShoppingCart(["Apple", "Banana", "Milk"])

print(cart[0])          
cart[1] = "Orange"      
print(cart[1])
print("---------------------------------------")


#Task 7: __del__ (Destructor Task)
class Session:
    def __del__(self):
        print ("Session Ended")
obj = Session()
print(obj)
del obj
print("---------------------------------------")

#Task 8: __contains__ (Membership Operator Task)
class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books

library = Library(["Python", "Java", "C++"])
print("Python" in library)  
print("ISE" in library)  

print("---------------------------------------")

#Task 9: __gt__, __lt__ (Comparison Task)
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    def __gt__(self, other):
        return self.salary > other.salary
        
    def __lt__(self, other):
        return self.salary < other.salary
    
e1 = Employee("Arpita", 50000)
e2 = Employee("JungKook", 60000)
print(e1 > e2)   
print(e1 < e2) 

print("---------------------------------------")

#Task 10: __iter__ and __next__ (Custom Iterator Task)
class Counter:
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

for i in Counter(1, 5):
    print(i)