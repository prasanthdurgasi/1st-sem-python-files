user_list = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_list.split()))
#total_sum = sum(numbers)
#average = total_sum / len(numbers)
print("Entered list:",numbers)
#print("Sum:", total_sum)
#print("Average:", average)
#numbers.reverse() 
#print("Reversed numbers:", numbers)
y=min(numbers)
z=max(numbers)
print("Minimum Element:",y)
print("Maximum Element:",z)

