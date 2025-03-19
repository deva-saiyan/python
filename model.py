def fact(n):
    if n == 0 or n == 1:
        return 1  # Fix: Ensure fact(1) returns 1
    return n * fact(n - 1)

i = True  # Control the loop

while i:
    num = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {num} is {fact(num)}")
    
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        i = False  # Stop the loop if the user doesn't say "yes"
