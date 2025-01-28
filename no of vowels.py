string = input("Enter a string: ")
vowels = "aeiouAEIOU"
length = len(string)
count = sum(string.count(vowel) for vowel in vowels)
num_spaces = string.count(' ')
print("number of characters:",length)
print("number of vowels:",count)
print("number of blank spaces : ",num_spaces)
