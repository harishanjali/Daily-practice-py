#palidromes from 1 to 1000

#method1
for i in range(1,1001):
    if(str(i)==str(i)[::-1]):
        print(i)
        
#method 2
i = 1
cnt=0
while i<=1000:
    j = i
    r = 0
    while j>0:
        d = j%10
        r = r*10+d
        j //= 10
    if(r==i):
        cnt+=1
        print(i,end=' ')
    i+=1
print()
print('Total palindroms are ',cnt)