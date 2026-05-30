
#threes number
#method 1
for i in range(100):
    if('3' in str(i)):
        print(i,end=' ')

#method 2
i = 1
while i<=300:
    n = i
    while n>0:
        d = n%10
        if(d==3):
            print(i,end=' ')
            break
        n//=10
    i+=1