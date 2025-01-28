def linear_search(l, n, element):
    for i in range(n):
        if l[i] == element:
            return i
    return -1 

n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))

element = int(input("Enter the element you want to search: "))
search = linear_search(l, n, element)

if search != -1:
    print(f"Element found at position {search+1}")
else:
    print("Element not found")
