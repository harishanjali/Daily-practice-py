y = [1,2,3,4,5,6,7,8,9,10]

x = 15


low = 0
high = len(y)-1

while low<=high:
    mid = low+(high-low)//2
    if y[mid]==x:
        print(True)
        break
    elif y[mid]<x:
        low = mid+1
    else:
        high = mid-1
else:
    print(False)