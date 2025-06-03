# Define two sets of colors
color = {'red', 'yellow', 'orange'}
paint = {'red', 'pink', 'blue', 'yellow', 'black', 'green'}

print("Original 'color' set:", color, '\n')

# Adding 'red' to 'color' set
# Since 'red' is already present, this won't change the set
color.add('red')
print("After adding 'red':", color, '\n')

# Removing 'yellow' from 'color' set
color.remove('yellow')
print("After removing 'yellow':", color, '\n')

# Perform intersection with 'paint' set and assign result back to 'color'
color = color.intersection(paint)
print("After intersection with 'paint':", color, '\n')

color = color.union(paint)
print("After union with 'paint':", color, '\n')

color = color.intersection_update(paint)
print("After intersection_update with 'paint':", color, '\n')
