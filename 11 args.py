# Function to add all numbers using a loop
def add(*args):
    a = 0
    for num in args:
        a += num
    return a

# Function to add all numbers using built-in sum()
def adds(*args):
    return sum(args)

# Calling the adds function
print(adds(2, 3, 4, 5, 6, 7, 7, 8, 3, 9, 435))

# Calling the add function
a = add(1, 2, 3, 4, 5, 6, 7, 8)
print(a)




def bdds(*kargs):
    return sum(kargs)

# Calling the adds function
print(bdds(2, 3, 4, 5, 6, 7, 7, 8, 3, 9, 435))




'''Feature	*args	**kwargs
Type Collected	Tuple	Dictionary
Accepts	Positional arguments	Keyword arguments
Use Case	When you don’t know how many positional arguments you'll get	When you don’t know the keyword args you'll get'''