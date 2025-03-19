
n = int(input("Enter a num : "))

def fact(n):
    if n == 0:
        return 1  # Base case
    
    return n * fact(n - 1)  # Recursive call


print(fact(n))  # )Output: 120
