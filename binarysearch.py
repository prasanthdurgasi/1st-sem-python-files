def binary_search(l, n, element, indices_sorted):
    low = 0
    high = n - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if l[mid] == element:
            print(f"Element is found at position {indices_sorted[mid]+1}")
            return 
        elif l[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    print("Element not found")

n = int(input("Enter the number of elements: "))
l = []
indices = []
for i in range(n):
    l.append(int(input(f"Enter element {i + 1}: ")))
    indices.append(i)

l_sorted = sorted(l)
indices_sorted = [i for _, i in sorted(zip(l, indices))]
element = int(input("Enter the element you want to search: "))
binary_search(l_sorted, n, element, indices_sorted)
#*List Comprehension `[i for _, i in sorted(zip(l, indices))]`**:
#This extracts only the indices from the sorted pairs.
#The `_` is a placeholder for the element in `l` (since we don't need it directly), and `i` is the original index from `indices`.
#So, for the sorted pairs `[(10, 1), (20, 2), (30, 0)]`, the list comprehension would produce `[1, 2, 0]`.