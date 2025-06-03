a = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,2,3,4,5,6,7,0]

s=map(lambda x:x**5 ,a)

d=filter(lambda x: x%2==0 , a)

f=map(lambda x: x**5 ,a)

ff=filter(lambda x: x%4==0 , a)

print(list(ff))
