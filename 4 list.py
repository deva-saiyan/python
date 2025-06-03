# Initial list of colors
color = ['red', 'yellow', 'green', 'blue']
print("Original Colors:", color)
print()

# Adding elements
color.append('orange')                       # Add to end
color.insert(0, 'white')                     # Add to beginning
color.extend(['skyblue', 'pink', 'navi'])    # Add multiple elements
print("After Adding Elements:", color)
print()

# Modifying an element
color[2] = 'apple'                           # Replace the element at index 2
print("After Modifying Index 2 to 'apple':", color)
print()

# Removing elements
color.pop()                                  # Remove last element
print("After pop():", color)
print()

color.remove('white')                        # Remove 'white' by value
print("After removing 'white':", color)
print()

# Reversing the list
color.reverse()
print("After reversing:", color)
print()

print("Count of 'red':", color.count('red'))
print("Index of 'green':", color.index('green'))  # Returns the first match
print()


# Working with a number list
num = [1, 2, 3, 3, 2, 4332, 344, 4, 5, 23, 6, 7, 8, 9, 10]

num.sort()                                   # Sort the list in ascending order
print("Sorted Numbers:", num)
print()

# Convert list to set (removes duplicates and unordered)
s = set(num)
print("Unique Numbers (Set):", s)


print("Max:", max(num))
print("Min:", min(num))
print("Sum:", sum(num))
print("Length:", len(num))
