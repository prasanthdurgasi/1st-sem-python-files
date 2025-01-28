def is_armstrong(number):
    total = 0
    num_str = str(number)
    power = len(num_str)
    
    for digit in num_str:
        total += int(digit) ** power
    
    return total == number

num =int(input("Enter the number:"))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
