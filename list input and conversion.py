user_list = input("Enter numbers separated by commas: ")
numbers = list(map(str, user_list.split(',')))
list_to_tuple = tuple(numbers)
print(numbers)
print(list_to_tuple)
