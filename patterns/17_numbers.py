rows = int(input('Enter no.of rows: '))


initial_value = 1
i = 1
while i <= rows:
    j = 1
    output = ''
    while j<=i:
        output += f'{initial_value}'
        initial_value+=1
        j+=1
    print(output)
    i+=1