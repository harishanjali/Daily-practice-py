x = 0
y = 1

while y<11:
    x = x+y
    x,y = y,x
    if(x%2==0):
        print(x)