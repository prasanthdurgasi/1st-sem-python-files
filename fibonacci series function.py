def fibonacci_series(n):
    if n <= 0:
        return []
    fib_series = [0]
    if n > 1:
        fib_series.append(1)
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

num_terms =int(input("Enter number of terms:"))
print("Fibonacci Series:", fibonacci_series(num_terms))
