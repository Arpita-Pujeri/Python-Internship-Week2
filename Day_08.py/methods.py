# Syntax
# class MyClass:
#     x = 10

#     @classmethod
#     def cmethod(cls):
#         pass

#     @staticmethod
#     def smethod(arg):
#         pass

class A:
    x=11
    def __init__(self):
        pass

    @classmethod
    def incrementation(cls):
        cls.x+=1

    @staticmethod
    def display_sum(a, b):
        print(a + b)

class B(A):
    def inc(self):
        A.x+=1
        print(A.x)

class C(A):
    def inc(self):
        A.x+=1
        print(A.x)

a=A()
print(a.x)

b=B()
b.inc()

c=C()
c.inc()

