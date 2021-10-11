import math
a=int(input("a\n"))
b=int(input("b\n"))
c=int(input("c\n"))
#a*(x**2)+(b*x)+c==0
D=(b**2)-(4*a*c)
if D>0:
    I1=((-b)+math.sqrt(D))/2*a
    I2=((-b)-math.sqrt(D))/2*a
    print(I1,I2)
elif D==0:
    I=-b/(2/a)
    print(I)
else:
    print("Нет корней")