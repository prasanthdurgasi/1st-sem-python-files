# 1. Creating a tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')

print("1. Created tuples:")
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# 2. Accessing tuple elements (indexing)
print("\n2. Accessing tuple elements:")
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# 3. Slicing a tuple
print("\n3. Slicing tuples:")
print("Slicing tuple1 (elements from index 1 to 3):", tuple1[1:4])
print("Slicing tuple2 (elements from index 1 onwards):", tuple2[1:])

# 4. Concatenation of tuples
print("\n4. Concatenation of tuples:")
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple1 and tuple2:", concatenated_tuple)

# 5. Repetition of a tuple
print("\n5. Repetition of a tuple:")
repeated_tuple = tuple1 * 3
print("Tuple1 repeated 3 times:", repeated_tuple)

# 6. Checking membership in a tuple
print("\n6. Checking membership:")
print("Is 3 in tuple1?", 3 in tuple1)
print("Is 'z' in tuple2?", 'z' in tuple2)

# 7. Length of a tuple
print("\n7. Length of a tuple:")
print("Length of tuple1:", len(tuple1))
print("Length of tuple2:", len(tuple2))

# 8. Counting the occurrence of an element in a tuple
print("\n8. Counting occurrences of an element:")
print("Occurrences of 3 in tuple1:", tuple1.count(3))
print("Occurrences of 'b' in tuple2:", tuple2.count('b'))

# 9. Finding the index of an element in a tuple
print("\n9. Finding index of an element:")
print("Index of 4 in tuple1:", tuple1.index(4))
print("Index of 'c' in tuple2:", tuple2.index('c'))

# 10. Tuple with one element (single element tuple)
print("\n10. Tuple with one element:")
single_element_tuple = (10,)
print("Single element tuple:", single_element_tuple)

# 11. Nested tuple
print("\n11. Nested tuple:")
nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)
print("Accessing nested tuple element (3rd element of nested tuple):", nested_tuple[2][0])

# 12. Iterating through a tuple
print("\n12. Iterating through a tuple:")
for item in tuple1:
    print("Item in tuple1:", item)

# 13. Converting a tuple to a list
print("\n13. Converting a tuple to a list:")
tuple_to_list = list(tuple1)
print("Tuple1 converted to list:", tuple_to_list)

# 14. Converting a list to a tuple
print("\n14. Converting a list to a tuple:")
list_to_tuple = tuple([6, 7, 8, 9])
print("List converted to tuple:", list_to_tuple)

# 15. Tuple unpacking
print("\n15. Tuple unpacking:")
a, b, c, d, e = tuple1
print("Tuple unpacking result: a =", a, ", b =", b, ", c =", c, ", d =", d, ", e =", e)

# 16. Creating an empty tuple
print("\n16. Creating an empty tuple:")
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 17. Joining two tuples (using join concept with an intermediate list)
print("\n17. Joining tuples using intermediate list:")
tuple3 = tuple([7, 8, 9])
joined_tuple = tuple(list(tuple1) + list(tuple3))
print("Joined tuple:", joined_tuple)

# 18. Tuple repetition with multiple values
print("\n18. Tuple repetition with multiple values:")
repeat_tuple = ('hello', 5) * 2
print("Repeated tuple:", repeat_tuple)

# 19. Sorting a tuple (tuple is immutable, but can convert to list to sort)
print("\n19. Sorting a tuple:")
tuple4 = (4, 1, 3, 5, 2)
sorted_tuple = tuple(sorted(tuple4))
print("Sorted tuple:", sorted_tuple)

# 20. Tuple comparison
print("\n20. Tuple comparison:")
tuple5 = (1, 2, 3)
tuple6 = (1, 2, 3)
print("Are tuple5 and tuple6 equal?", tuple5 == tuple6)
tuple7 = (1, 2, 4)
print("Are tuple5 and tuple7 equal?", tuple5 == tuple7)

