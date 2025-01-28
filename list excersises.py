# 1. Creating a list
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']

print("1. Created lists:")
print("List1:", list1)
print("List2:", list2)

# 2. Accessing list elements (indexing)
print("\n2. Accessing list elements:")
print("First element of list1:", list1[0])
print("Last element of list2:", list2[-1])

# 3. Slicing a list
print("\n3. Slicing lists:")
print("Slicing list1 (elements from index 1 to 3):", list1[1:4])
print("Slicing list2 (elements from index 1 onwards):", list2[1:])

# 4. Concatenation of lists
print("\n4. Concatenation of lists:")
concatenated_list = list1 + list2
print("Concatenated list1 and list2:", concatenated_list)

# 5. Repetition of a list
print("\n5. Repetition of a list:")
repeated_list = list1 * 3
print("List1 repeated 3 times:", repeated_list)

# 6. Checking membership in a list
print("\n6. Checking membership:")
print("Is 3 in list1?", 3 in list1)
print("Is 'z' in list2?", 'z' in list2)

# 7. Length of a list
print("\n7. Length of a list:")
print("Length of list1:", len(list1))
print("Length of list2:", len(list2))

# 8. Counting the occurrence of an element in a list
print("\n8. Counting occurrences of an element:")
print("Occurrences of 3 in list1:", list1.count(3))
print("Occurrences of 'b' in list2:", list2.count('b'))

# 9. Finding the index of an element in a list
print("\n9. Finding index of an element:")
print("Index of 4 in list1:", list1.index(4))
print("Index of 'c' in list2:", list2.index('c'))

# 10. List with one element (single element list)
print("\n10. List with one element:")
single_element_list = [10]
print("Single element list:", single_element_list)


# 11. Iterating through a list
print("\n11. Iterating through a list:")
for item in list1:
    print("Item in list1:", item)

# 12. Converting a list to a tuple
print("\n12. Converting a list to a tuple:")
list_to_tuple = tuple(list1)
print("List1 converted to tuple:", list_to_tuple)

# 13. Converting a tuple to a list
print("\n13. Converting a tuple to a list:")
tuple_to_list = list(('a', 'b', 'c'))
print("Tuple converted to list:", tuple_to_list)

# 14. List unpacking
print("\n14. List unpacking:")
a, b, c, d, e = list1
print("List unpacking result: a =", a, ", b =", b, ", c =", c, ", d =", d, ", e =", e)

# 15. Creating an empty list
print("\n15. Creating an empty list:")
empty_list = []
print("Empty list:", empty_list)

# 16. Joining two lists (using an intermediate string or list)
print("\n16. Joining lists using intermediate list:")
list3 = [7, 8, 9]
joined_list = list1 + list3
print("Joined list1 and list3:", joined_list)

# 17. List repetition with multiple values
print("\n17. List repetition with multiple values:")
repeat_list = ['hello', 5] * 2
print("Repeated list:", repeat_list)

# 18. Sorting a list
print("\n18. Sorting a list:")
list4 = [4, 1, 3, 5, 2]
sorted_list = sorted(list4)
print("Sorted list:", sorted_list)

# 19. List comparison
print("\n19. List comparison:")
list5 = [1, 2, 3]
list6 = [1, 2, 3]
print("Are list5 and list6 equal?", list5 == list6)
list7 = [1, 2, 4]
print("Are list5 and list7 equal?", list5 == list7)

# 20. Modifying list elements
print("\n20. Modifying list elements:")
list1[0] = 10  # Change the first element
print("Modified list1:", list1)

# 21. Adding elements to a list
print("\n21. Adding elements to a list:")
list1.append(6)
print("List1 after appending 6:", list1)

# 22. Removing elements from a list
print("\n22. Removing elements from a list:")
list1.remove(10)  # Removes first occurrence of 10
print("List1 after removing 10:", list1)

# 23. Popping an element from a list
print("\n23. Popping an element from a list:")
popped_element = list1.pop()
print("Popped element:", popped_element)
print("List1 after pop:", list1)

# 24. Reversing a list
print("\n24. Reversing a list:")
reversed_list = list1[::-1]
print("Reversed list1:", reversed_list)

