l = [0,1,2,3,4,5,6,7,8,9]
def binary_serch(l,item):
    low = 0
    high = len(l)-1
    while low <=high:
        mid = (low+high)/2
        guess = l[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid+1
    return None
print(binary_serch(l,3))

arr = [ 3, 4, 5, 6, 44, 32, 22, 22 ]
x = 22
def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    else :
        return binary_search_recursive(arr, elem, mid+1, end)

print(binary_search_recursive(arr = [ 3, 4, 5, 6, 22, 32 ],elem= 22))
