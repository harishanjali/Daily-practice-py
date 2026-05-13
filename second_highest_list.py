list_a = [5,5,-5,5,5,-1]
n = set(list_a)
print(n)
first = float('-inf')#list_a[0]
second = float('-inf')#list_a[1]

for i in list_a:
    if i>first:
        second = first
        first = i
    if i>second and i<first:
        second = i
print(second)