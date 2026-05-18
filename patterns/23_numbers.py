rows = int(input('Enter number of rows: '))

i = 1
while i <= rows:
    j = i
    output = ''
    while j >=1:
        output+=f'{j}'
        j-=1
    i+=1
    print(output)

