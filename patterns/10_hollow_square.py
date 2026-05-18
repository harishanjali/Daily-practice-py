rows = int(input("Enter number of rows: "))

i = 0
while i < rows:
    if(i==0 or i == rows-1):
        print("*"*rows)
    else:
        print("*"+(" "*(rows-2))+"*")
    i+=1