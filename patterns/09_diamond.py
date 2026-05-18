rows = int(input('Enter no of rows: '))

i = 0
j = 1
while i < rows:
    # print(i==rows-1,i)
    print((' '*(rows-i))+'*'*j)
    i += 1
    j+=2

k=1
j-=4
while k <= rows:
    print((' '*(k+1))+'*'*j)
    k+=1
    j-=2