binary_number = int(input('Enter binary number to convert: '))

decimal_number = 0
index = 0
while binary_number>0:
    d = binary_number%10
    decimal_number = decimal_number + (d*(2**index))
    index += 1
    binary_number = binary_number//10
print(decimal_number)