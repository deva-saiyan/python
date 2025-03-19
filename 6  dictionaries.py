# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science"
}

print(student)  
# Output: {'name': 'John', 'age': 21, 'course': 'Computer Science'}

#Access values

print(student["name"])  # Output: John
print(student.get("age"))  # Output: 21

# add update elements
student["age"] = 22  # Update age
student["city"] = "New York"  # Add a new key-value pair

print(student)
# Output: {'name': 'John', 'age': 22, 'course': 'Computer Science', 'city': 'New York'}



student = {"name": "Alice", "age": 23, "grade": "A"}

print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])
print(student.values())  # Output: dict_values(['Alice', 23, 'A'])
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 23), ('grade', 'A')])


# Loop through keys
for key in student:
    print(key, ":", student[key])

# Loop through keys and values
for key, value in student.items():
    print(f"{key}: {value}")




student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science"
}

student.pop("age")  # Removes 'age' key
print(student)

del student["course"]  # Deletes 'course' key
print(student)

student.clear()  # Removes all elements
print(student)  # Output: {}
