rows = int(input('Enter no of rows: '))

i = 1
spaces = 0
while i <= rows:
    if(i==1):
        print('*')
    elif(i==rows):
        print('* '*rows)
    else:
        spaces += 2
        print('*'+(' '*(spaces))+'*')
    i += 1
