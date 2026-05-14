n = 2
cnt=0
while True:
    i = 2
    while i<=n//2:
        if(n%i==0):
            break
        i+=1
    else:
        cnt+=1
        print(n)
        if(cnt==1000):
            break
    n+=1