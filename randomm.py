import random


while True:
    try:
        lenthh = int(input("input the lenth of password you want\n"))
        break
    except ValueError:
        lenthh = int(input("that shoul be just a number"))
        continue

def contains(lenth):
    
    lower = "abcdefghijklmnopqstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPSTUVWXYZ"
    num = "0123456789"
    symbol = "_.-"
    togetherhard = lower+UPPER+num+symbol
    togetherlight = lower+UPPER+num+symbol  
    cont = input("you want this password would be hard or easy, print HARD or EASY\n")
    if cont == "HARD":
        password = "".join(random.sample(togetherhard,lenth))
    elif cont == "EASY":
        password = "".join(random.sample(togetherlight,lenth))
    else: 
        password = "".join(random.sample(togetherhard,lenth))
    
    yield password

if __name__ == "__main__":
    pas = iter(contains(lenthh))
    print(next(pas))
