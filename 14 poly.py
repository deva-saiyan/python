class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()  # Calls the correct method based on the object passed

dog = Dog()
cat = Cat()
animal = Animal()

make_sound(dog)    # Output: Bark
make_sound(cat)    # Output: Meow
make_sound(animal) # Output: Some generic animal sound


def add(a=0 , b=0 ,c=0):
   total=a+b+c
   return total

print(add(1,2))