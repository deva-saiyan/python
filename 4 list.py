fruits = ['apple', 'orange', 'mango', 'banana' , 'apple']

print(len(fruits))
print('apple' in fruits)

fruits.append("1")
fruits.extend(['2','3','4'])
fruits.insert(0 , '0')

fruits.pop()
fruits.remove('apple')
fruits[2]="onion" # replace
 
del fruits[0] # delete
#fruits.clear() #clear

b = []
c = [b.append(i.capitalize()) for i in fruits]

print(b)

c=[]
[c.append(i.upper()) for i in fruits]
print(sorted(c))

v=[1,2,3,4,3]
v.reverse()
print(v)