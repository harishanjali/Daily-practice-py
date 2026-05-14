number = int(input('Enter number: '))
#to_str = str(number)
#result = to_str[-1]+to_str[1:-1]+to_str[0]

bkp_number = number
last_num = number%10
power = 1
while number>=10:#T T 1234
    number = number//10 #123 12
    power *= 10 #10 100
    print(number,power)
first_num = number%10
middle = (bkp_number % power) // 10
print(middle)
result = (last_num*power) + (middle*10) + first_num
# print(result)