print("wel come to my Program")
x = int(input('Enter numbers of row :'))
for i in range(0, x):
    for j in range(0, i+1):
        print('*', end=' ')
    print(' ')
for i in range(x, 0, -1):
    for j in range(1, i):
        print('*', end=' ')
    print(' ')
