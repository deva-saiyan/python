a =4

def fact(x):
    if x==0 or x==1:
        return x
    return x * fact(x-1)

print(fact(a))



