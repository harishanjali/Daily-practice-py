rows = int(input('Enter number of rows: '))

while rows >= 1:
    chr_num = 65
    i=1
    output = ''
    while i<=rows:
        output += chr(chr_num)
        chr_num += 1
        i+=1
    rows-=1
    print(output)
