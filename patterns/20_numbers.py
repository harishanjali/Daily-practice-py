rows = int(input('Enter no.of rows: '))

i = 1
while rows >= i:
    output = ''
    j = 1
    while j<=rows:
        output += f'{rows}'
        j+=1
    print(output)
    rows -= 1

