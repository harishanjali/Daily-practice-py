rows = int(input('Enter no.of rows: '))

i = 1
while i<=rows:
    j=i
    output = ''
    while j>1:
        output += f'{j}'
        j-=1
    k = 1
    while k<=i:
        output+=f'{k}'
        k+=1
    print(output)
    i+=165

        
