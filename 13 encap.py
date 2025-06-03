'''Private variables can't be accessed directly from outside.

Getter and Setter methods provide controlled access.

This protects the data and hides implementation details.'''


class Person:
    def __init__(self, name, age):
        self.__name = name      # private variable
        self.__age = age        # private variable

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    # Public method
    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


p = Person("Alice", 30)

p.display()        # Name: Alice, Age: 30

print(p.get_age()) # 30

p.set_age(35)      
p.display()        # Name: Alice, Age: 35

p.set_age(-5)      # Age must be positive

# Direct access to private variables will cause an error:
# print(p.__age)   # AttributeError
