# Original string
word = 'hello my name is Deva '

# Basic information about the string
print("Original String:", word)
print("Length:", len(word))             # Includes spaces
print("Type:", type(word))              # Type of the variable
print()

# Case conversions
print("Upper Case:", word.upper())      # All characters to uppercase
print("Lower Case:", word.lower())      # All characters to lowercase
print("Title Case:", word.title())      # Capitalize each word
print()

# Replace a word in the string
modified_word = word.replace('Deva', 'raj')
print("After Replacement:", modified_word)
print()

# String slicing and reversing
print("Reversed String:", word[::-1])       # Reverse the entire string
print("Slice [1:7]:", word[1:7])            # Characters from index 1 to 6
print("Slice [-2:-13]:", word[-2:-13])      # Empty string (invalid range)
print()

# Uppercase part of the string
print("First 13 Characters in Uppercase:", word[0:13].upper())

# Reversing word order
reversed_words = ' '.join(word.split()[::-1])
print("Words Reversed:", reversed_words)
print()


print("Strip:", word.strip())     # Removes leading/trailing spaces
print("Left Strip:", word.lstrip())  # Removes leading spaces
print("Right Strip:", word.rstrip())  # Removes trailing spaces
