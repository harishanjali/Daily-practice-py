nth_prime = int(input('Enter number: '))
number = 2
total_count = 0
while True:
    count = 0
    i = 2
    while i<=number//2:
        if(number%i==0):
           break
        i+=1
    else:
        total_count += 1
        if(total_count == nth_prime):
            print(number)
            break
    number += 1