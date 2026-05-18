rows = int(input('Enter number of rows: '))

while rows>=1:
    j=1
    output = ''
    while j<=rows:
        output += f'{j}'
        j+=1
    print(output)
    rows -= 1