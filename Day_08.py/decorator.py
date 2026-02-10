# Syntax
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # pre-processing
#         result = func(*args, **kwargs)
#         # post-processing
#         return result
#     return wrapper

# @decorator
# def some_function(...):

def login(decorated):
    def wrapper(user, password):
        if user == "admin" and password == "1234":
            print("Login successful")
            decorated(user, password)
        else:
            print("Login failed")
    return wrapper

@login
def login_page(user, password):
    print("welcome to the dashboard")

login_page("admin", "1234")
login_page("someone", "bad")


print("----------------------------------")

import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print("Elapsed:", end - start)
    return wrapper

@execution_time
def first_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("sum :", total)

first_n(1000000)

