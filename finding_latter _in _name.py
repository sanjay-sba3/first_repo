x = str(input("enter your name:"))
y = str(input('enter letter to find:'))
c = 0
for i in x:
    if i == y:
        c = c + 1
print('There are', c, 'numbers of', '"', y, '"', 'present in name', '"', x, '"')
