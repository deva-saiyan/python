from model import *


i = True  # Control the loop
while i:
    num = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {num} is {fact(num)}")
    
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        i = False  # Stop the loop if the user doesn't say "yes"
