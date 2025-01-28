a = int(input("Enter any number: "))
b = a
num = len(str(a))
rev = 0

while a > 0:
    rem = a % 10
    rev+= rem**num
    a = a // 10  

if rev == b:
    print("The given number is a armstrong.")
else:
    print("The given number is not a armstrong.")
