rows = int(input('Enter no.of rows: '))

i = 1
while rows >= i:
    j = 1
    output = ''
    while j<=rows:
        output += f'{j}'
        j+=1
    rows -= 1
    print(output)