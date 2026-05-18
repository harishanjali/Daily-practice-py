rows = int(input('Enter no of rows: '))

i = 0

stars = rows+(rows-1)
spaces = 0
while i < rows:
    print((' '*spaces)+('* '*stars))
    stars -= 2
    i += 1
    spaces += 2
