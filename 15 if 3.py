list = [1,2,3,4,5,6,7,8,9,10]

for num in list:
    if num == 2:
        pass  # Reserved, maybe logic will be added later
    elif num == 5:
        continue  # Skip 5
    elif num == 7:
        break     # Stop loop at 7
    print(num)

