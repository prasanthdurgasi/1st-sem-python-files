def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1) 

def fact_function():
    number = int(input("Enter the number: ")) 
    factorial = fact(number)
    print(f"Factorial of {number} is {factorial}")

fact_function()
