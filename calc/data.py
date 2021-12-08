import sympy as sym

def calculate(ex):
    x = sym.expand(ex)
    return x

def remember_result(num):
    x = num
    return x

def add(num,memb):
    x = num + memb
    return x

def minus(num,memb):
    x = memb - num
    return x

def multiply(num,memb):
    x = num * memb
    return x

def division(num,memb):
    if num == 0:
        return print("DONT do that")
    else:
        x = memb / num
        return x