x = input("Enter a string: ")
y = ''.join(reversed(x)) 
print("Reversed String:",y)
if(x==y):
    print("given string is palindrome:")
else:
    print("given string is not palindrome:")