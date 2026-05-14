#strong number
# the sum of factorial of number is equals the number
n = int(input('ENter number: '))
bkp_num=n
total_sum = 0
while n>0:
    d = n%10
    i = 1
    factorial = 1
    while i<=d:
        factorial *=i
        i+=1
    total_sum+=factorial
    n=n//10
if(total_sum==bkp_num):
    print('strong number')
else:
    print('not strong number')