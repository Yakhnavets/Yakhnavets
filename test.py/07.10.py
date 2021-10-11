def looping(l):
     l = iter(l)
     min = max = next(l)
     for i in l:
         if i < min: min = i
         if i > max: max = i
     return min, max
#найти самый большой и маленький)
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]