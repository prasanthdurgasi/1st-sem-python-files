print("Various operations on string using string libraries:")
# Sample string
sample_string = " Hello, World! "
# 1. Length of the string
length = len(sample_string)
# 2. Convert to uppercase
uppercase = sample_string.upper()
# 3. Convert to lowercase
lowercase = sample_string.lower()
# 4. Strip whitespace
stripped = sample_string.strip()
# 5. Replace a substring
replaced = sample_string.replace("World", "Python")
# 6. Split the string into a list
split_list = sample_string.split(", ")
# 7. Join a list back into a string
joined_string = " - ".join(split_list)
# 8. Find the index of a substring
index_of_world = sample_string.find("World")
# 9. Count occurrences of a character
count_o = sample_string.count("o")
# 10. Check if the string starts with a specific substring
starts_with_hello = sample_string.startswith(" Hello")
# 11. Check if the string ends with a specific substring
ends_with_exclamation = sample_string.endswith("!")
# 12. Accessing a character by index
first_char = sample_string[0]
# Print results
print("Original string:", sample_string)
print("Length:", length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Stripped:", stripped)
print("Replaced:", replaced)
print("Split list:", split_list)
print("Joined string:", joined_string)
print("Index of 'World':", index_of_world)
print("Count of 'o':", count_o)
print("Starts with ' Hello':", starts_with_hello)
print("Ends with '!':", ends_with_exclamation)
print("First character:", first_char)
