number = int(input('enter number: '))

rows = (number*2)-1

i = 1
while i <=number:
    j = 1
    output = ''
    while j<=i:
        output += f'{j}'
        j+=1
    k = i-1
    while k >= 1:
        output+= f'{k}'
        k-=1
    print(output)
    i+=1
number = rows-number
while number >= 1:
    j = 1
    output = ''
    while j<=number:
        output += f'{j}'
        j+=1
    k = number-1
    while k >= 1:
        output+= f'{k}'
        k-=1
    print(output)
    number -= 1
