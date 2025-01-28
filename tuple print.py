user_list = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_list.split(',')))
length = len(numbers)
half = length // 2
first = numbers[:half]
next = numbers[half:]
print(first)
print(next)
