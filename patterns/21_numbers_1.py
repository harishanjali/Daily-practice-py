num = int(input('Enter number of rows: '))

i = 1
while i <= num:
    j = i
    output = ''
    while j<=num:
        output += f'{j}'
        j+=1
    print(output)

    i+=1

i = 1    
while i < num:
    j = num - i
    output = ''
    while j<=num:
        output += f'{j}'
        j+=1
    print(output)
    i+=1
