a = 1
b = 5

try:
    if a == 10:
        print(b)

except Exception as e:
    print(f'Error: {e}')

else:
    print('Code OK')

finally:
    print('Executed')
