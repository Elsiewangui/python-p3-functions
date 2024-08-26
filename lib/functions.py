#!/usr/bin/env python3

def greet_programmer():
  print("Hello, programmer!")



def greet(name):
    print(f"Hello, {name}!")
greet("Elsie")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Elsie")

def add(a, b):
    return a+b
print(add(4,6))

def halve(number):
    if type(number)in (int, float):
        return number / 2
    else:
        return None
print(halve(30))
print(halve("number"))
