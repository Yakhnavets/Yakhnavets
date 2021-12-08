#lst = [1,2,3,4,5,6,64,3,2,98,7,7,7,7,5]
num = str(input("Input the list of numbers\n"))
lst = []
def isnum(lst):    
    for i in lst.split(","):
        if i == int(i):
            return 

while True:
    try:
        isnum(num)
        break
    except ValueError:
        num = str(input("THE LIST OF NUMBERS LIKE:\n 1,2,3,4,5\n"))
        continue

for i in num.split(","):
    lst.append(int(i))

def range(lst):
    lst = sorted(set(lst))
    
    range  = (list(lst))
    range.append(99999999999999)
    
    text = ""
    
    current = 0
    tiktok = 1
    last = None

    while True:
        if len(range)-1 == current:
            break
        if range[current] >= range[current+1] - tiktok:
            last = range[current+1]
            del range[current+1]
            tiktok += 1
        else:
            text += str(range[current])
            if range[current] == last or last == None:
                text += ", " 
            else:       
                text += "-" + str(last)+ ", "
            tiktok = 1
            current += 1
            last = None
    print (text[:-2])
range(lst)