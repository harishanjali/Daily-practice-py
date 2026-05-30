#aaabccaa

x = 'aaabccaac'

count = 1
output = ''
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count+=1
    else:
        output += x[i] + str(count)
        count = 1
else:
    output += x[i] + str(count)
print(output)

