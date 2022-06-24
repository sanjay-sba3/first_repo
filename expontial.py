import math


def exp(x):
    n = 5999
    t_sum = 0
    for i in range(n):
        term = x**i / math.factorial(i)
        t_sum = t_sum + term

    return t_sum

e = exp(1)

# Displaying result
print("e = ", e)