l=[1,2,3,4,5,6,5,4,3,2,1,7,8,9,10]
a=[]
b=[]
for i in l:
    if  i not in b:
        b.append(i)
    else:
        a.append(i**50)
print(b)
print(a)

print(list(reversed(b)))

c=[]
d=0
e=0
for i in l:
    if i%2==0 and i>d:
        d=i
    else:
        e=i
print(sorted(l))