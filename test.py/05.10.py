a = input("Введите уравнение типа y=4x-5\n")
x = input("Введите значение X\n")
eq = a.split("=")
coeff = eq[1].split("x")
res = int(coeff[0]*int(x)+ int(coeff[1]))
print(res)
# if coeff