a = int(input("Enter any number: "))
b = a
rev = 0

while a > 0:
    rem = a % 10
    rev = rev * 10 + rem
    a = a // 10  

if rev == b:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")
