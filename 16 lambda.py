a = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,2,3,4,5,6,7,0]

add = map (lambda x:x**2 , a)

even = filter(lambda x : x%2==0,a)

print(list(even))