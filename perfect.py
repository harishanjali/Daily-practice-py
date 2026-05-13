#n = int(input('Enter a number: '))
#if sum of the divisors of a number is equals the number, then it is perfect number
n = 12
cnt=0
while True:
    d = 1
    s = 0
    while d<=n//2:
        if n%d==0:
            s+=d
        d+=1
    if(s==n):
        cnt+=1
        print('perfect',n)
        if(cnt==10):
            break
    # else:
    #     print('Not perfect')
    n+=1