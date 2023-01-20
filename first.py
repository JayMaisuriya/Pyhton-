import math

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def multi(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

def modulo(x,y):
    return(x%y)

def square(x):
    return(x**2)

def fact(x):
    if x==0:
        return 1
    else:
        return (x*fact(x-1))