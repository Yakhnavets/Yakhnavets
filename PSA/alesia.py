import re
path = input()
file_out = open("new.py", "wt")

file_in = open(path,"r")
for line in file_in:
    if "cast(" in line:
        lin = line[:line.find("cast")-1:]
        lin+= line[line.find(",")+1::]
        file_out.write(lin.replace(')', '') )
    else:
        file_out.write(line)

    #file_out.write(re.sub('(=\scast)([])', " "), file_in)


file_in.close()
file_out.close()