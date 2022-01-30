x = int(input('Enter numbers of rows : '))
k = x+1
for i in range(0, x+1):
    for j in range(0, k):
        print(end=' ')
    k = k-1
    for j in range(0, i+1):
        print('*', end=' ')
    print(' ')
k = k+2
for i in range(x, 0 ,-1):
    for j in range(0, k):
        print(end=' ')
    k = k+1
    for j in range (i, 0, -1):
        print('*', end=' ')
    print(' ')
print("thank you ")    
