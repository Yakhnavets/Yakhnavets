st = 'ab3(#$%[pop]cvfs){kek}'
list = []
for i in st:
    list.append(i)

def brackets(string):
    open = []
    
    for i in range(len(string)):
        if i == "(" or i == "{" or i == "[":
            open.append(i)
            continue
        if (string[i] == ")" or string[i] == "}" or string[i] == "]") and open:
            if (open[-1]+ string[i]== "()") or (open[-1]+ string[i]== "{}") or (open[-1]+ string[i]== "[]"):
                string.pop()
            else:
                return False
        else:
            return False
    if string == []:
        return True        

print(brackets(list))

