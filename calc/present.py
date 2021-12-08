import bl as bl
def show_message(mess):
    print(mess)

def init():
    #expession = input("Input the expression\n")
    expression = "1-(2*3)*(14+(4-5))"
    result = bl.calculate(expression)
    show_message(f"result is:\n{result}")

                       
init() 




