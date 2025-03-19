add = lambda x, y: x + y
print(add(5, 3))

a=[1,2,3,4,5]


aa=list(map(lambda x : x*x ,a))

aaa = list(filter(lambda x: x%2==0 ,a))

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x , nums)
print(product)


print(aaa)