#!/usr/bin/env python

def addition(a,b):
    add = a+b
    return(add)

def substraction(a,b):
    sub = a-b
    return(sub)

def multiplacation(a,b):
    mult = a*b
    return(mult)

def division(a,b):
    div = a/b
    return(div)

oper = 0
operators=("+-*/")


while True:
    try:
        a = int(input("Enter a number or a letter to exit: "))
        oper = input("Enter an operation: ")
        while oper not in operators:
            oper = input("Enter an operation: ")
        b = int(input("Enter another number: "))
        if oper == "+":
            print("Result: %d\n" % (addition(a,b)))
        elif oper == "-":
            print("Result: %d\n" % (substraction(a,b)))
        elif oper == "*":
            print("Result: %d\n" % (multiplacation(a,b)))
        elif oper == "/":
            if b == 0:
                print("We cant divide with 0.\n")
            else:
                print("Result %f\n" % (division(a,b)))
    except ValueError:
        exit()
