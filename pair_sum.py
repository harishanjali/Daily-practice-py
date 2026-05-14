x = [1,2,3,4,5,6,7]

target = int(input('Enter num: '))

for i in x:
    for j in x:
        if(i+j==target):
            print(i,j)