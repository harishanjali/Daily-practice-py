rows = int(input('Enter no.of rows: '))

i = 1
while i <= rows:
    j = 1
    output = ''
    while j<=i:
        output += f'{j}'
        j+=1
    i+=1
    print(output)