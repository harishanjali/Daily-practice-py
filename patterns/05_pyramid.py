num_of_rows = int(input('Enter no.of rows: '))

i = 0
stars = 1
spaces = num_of_rows + 1
while i < num_of_rows:
    print((' '*(spaces-stars))+('* ')*stars)
    stars += 2
    i += 1

#this problem is pending