# Assignment 5
# Task 3
# Given variable
str = "The quick brown fox jumps over the lazy dog"

# a. Print the string to the page
print(str)

# b. Print the length of the string to the page
print(len(str))

# c. Print the string in all uppercase letters
print(str.upper())

# d. Print the string in all lowercase letters
print(str.lower())

# e. Print the string in title case
print(str.title())

# f. Print the string in reverse
print(str[::-1])

# g. Print the string in reverse title case
print(str[::-1].title())

# h. Count the number of times the letter “a” appears in the string
print(str.count('a'))

# i. Count the number of times the word “the” appears in the string
print(str.lower().count('the'))

# j. Replace the word “the” with the word “a”
print(str.replace('the', 'a'))

# Task 4
# Count the frequency of each letter in the string and save the results in a dictionary
my_str = "The quick brown fox jumps over the lazy dog"
frequency_letter = {}
my_str = my_str.lower() # Make the string lowercase

for letter in my_str:
    if letter.isalpha():  # Checks if it's a letter
        if letter not in frequency_letter:
            frequency_letter[letter] = my_str.count(letter)
            
print(frequency_letter)

# Task 5
# Given the below lists
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

# Interpolating the three lists into strings
for i in range(len(people)):
    print(f"{people[i]} the {sex[i]} is {age[i]} years old.")
