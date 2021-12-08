import data as dt

def brackets(_str):
    bracket = []
    open = True
    index = 0
    while index < len(_str) and open:
        token = _str[index]
        if token == "(":
            bracket.append(token)
        elif token == ")":
            if len(bracket) == 0:
                open = False
            else:
                bracket.pop()
        index +=1
    return open and len(bracket) == 0

def check_number(ex):
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*", "(", ")"]
    for i in range (len(ex)):
        if ex[i] == ")" and ex [i-1] in ["+", "-", "/", "*"]:
            return False
        if ex[i] in lst and ex[-1] not in ["+", "-", "/", "*"]:
            continue
        else:
            return False
    return True

def calculate(ex):
    if brackets(ex) is True and check_number(ex) is True:
        result = dt.calculate(ex)
        return float(result)
    else:
        return -1

def add(num,memb):
    if brackets(num) is True and check_number(num) is True:
        num = dt.calculate(num)
        result = dt.add(num,memb)
        return float(result)
    else:
        return -1

def minus(num,memb):
    if brackets(num) is True and check_number(num) is True:
        num = dt.calculate(num)
        result = dt.minus(num,memb)
        return float(result)
    else:
        return -1


def multiply(num,memb):
    if brackets(num) is True and check_number(num) is True:
        num = dt.calculate(num)
        result = dt.multiply(num,memb)
        return float(result)
    else:
        return -1

def division(num,memb):
    if brackets(num) is True and check_number(num) is True:
        num = dt.calculate(num)
        result = dt.division(num,memb)
        return float(result)
    else:
        return -1