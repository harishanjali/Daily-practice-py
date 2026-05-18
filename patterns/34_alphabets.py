rows = int(input('enter number of rows: '))

chr_num = 64+rows

i = 0
while i<=rows:
    print(chr(chr_num)*(rows-i))
    i+=1
    chr_num -= 1
    #print('test')
