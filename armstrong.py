#armstrong number
'''a positive integer equal to the sum of its 
own digits each raised to the power of the total number of digits'''

n = int(input('Enter a number: '))
bkp_num_1 = n
bkp_num_2 = n
power = 0
while n>0:
    n //= 10
    power+=1

total_sum = 0
while bkp_num_1>0:
    d = bkp_num_1%10
    i = 1
    powered_value = 1
    while i<=power:
        powered_value*=d
        i+=1
    total_sum+=powered_value
    bkp_num_1//=10
if(bkp_num_2==total_sum):
    print('armstrong number')
else:
    print('not armstrong number')
