number = int(input('Enter a number: '))

check = number
reverse = 0
while number>0:
    d = number%10
    reverse = reverse*10+d
    number = number//10
if(reverse==check):
    print('Palindrome')
else:
    print('Not a palindrome')