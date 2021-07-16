name = input('Enter a name: ')
rev = name[::-1]
if name == rev:
    print(f'{name}, {rev}, Palindrome')
else:
    print(f'{name} not a palindrome')