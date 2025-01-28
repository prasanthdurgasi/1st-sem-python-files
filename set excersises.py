# 1. Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = {'a', 'b', 'c', 'd'}

print("1. Created sets:")
print("Set1:", set1)
print("Set2:", set2)

# 2. Adding an element to a set
print("\n2. Adding an element to a set:")
set1.add(6)
print("Set1 after adding 6:", set1)

# 3. Removing an element from a set (using remove and discard)
print("\n3. Removing an element from a set:")
set1.remove(4)  # Will raise KeyError if element doesn't exist
print("Set1 after removing 4:", set1)

# Using discard which won't raise an error if element doesn't exist
set2.discard('z')  # No error even though 'z' doesn't exist
print("Set2 after discarding 'z' (no error if element doesn't exist):", set2)

# 4. Checking membership in a set
print("\n4. Checking membership in a set:")
print("Is 3 in set1?", 3 in set1)
print("Is 'x' in set2?", 'x' in set2)

# 5. Length of a set
print("\n5. Length of a set:")
print("Length of set1:", len(set1))
print("Length of set2:", len(set2))

# 6. Set Union (combining two sets)
print("\n6. Set Union (combining two sets):")
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# 7. Set Intersection (common elements between two sets)
print("\n7. Set Intersection (common elements between two sets):")
set3 = {3, 4, 5, 6}
intersection_set = set1.intersection(set3)
print("Intersection of set1 and set3:", intersection_set)

# 8. Set Difference (elements in set1 but not in set3)
print("\n8. Set Difference (elements in set1 but not in set3):")
difference_set = set1.difference(set3)
print("Difference of set1 and set3:", difference_set)

# 9. Set Symmetric Difference (elements that are in either set1 or set3 but not both)
print("\n9. Set Symmetric Difference:")
symmetric_difference_set = set1.symmetric_difference(set3)
print("Symmetric Difference between set1 and set3:", symmetric_difference_set)

# 10. Set Subset (checking if set1 is a subset of set3)
print("\n10. Set Subset:")
print("Is set1 a subset of set3?", set1.issubset(set3))

# 11. Set Superset (checking if set1 is a superset of set3)
print("\n11. Set Superset:")
print("Is set1 a superset of set3?", set1.issuperset(set3))

# 12. Set Disjoint (checking if two sets have no common elements)
print("\n12. Set Disjoint:")
print("Are set1 and set3 disjoint?", set1.isdisjoint(set3))

# 13. Set Copy
print("\n13. Set Copy:")
set4 = set1.copy()
print("A copy of set1:", set4)

# 14. Set Clearing (removing all elements from a set)
print("\n14. Set Clearing:")
set1.clear()
print("Set1 after clearing:", set1)

# 15. Iterating through a set
print("\n15. Iterating through a set:")
for item in set2:
    print("Item in set2:", item)

# 16. Set from a list (removing duplicates automatically)
print("\n16. Set from a list (removing duplicates automatically):")
list_with_duplicates = [1, 2, 3, 4, 4, 5, 5, 6]
unique_set = set(list_with_duplicates)
print("Set from list_with_duplicates:", unique_set)

# 17. Set Intersection with a different approach (using & operator)
print("\n17. Set Intersection with & operator:")
intersection_set2 = set1 & set3
print("Intersection of set1 and set3 using &:", intersection_set2)

# 18. Set Union with a different approach (using | operator)
print("\n18. Set Union with | operator:")
union_set2 = set1 | set3
print("Union of set1 and set3 using |:", union_set2)

# 19. Set Difference with a different approach (using - operator)
print("\n19. Set Difference with - operator:")
difference_set2 = set1 - set3
print("Difference of set1 and set3 using -:", difference_set2)

# 20. Set Symmetric Difference with a different approach (using ^ operator)
print("\n20. Set Symmetric Difference with ^ operator:")
symmetric_difference_set2 = set1 ^ set3
print("Symmetric Difference between set1 and set3 using ^:", symmetric_difference_set2)

