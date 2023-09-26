import math

def sin_approx(x):
    sum = 0
    j = 0
    for i in range(1,27,2):
        sum += ((x**i) / math.factorial(i)) * ((-1)**j)
        j += 1
    return print(f'sin({x}) approximation is {sum}')

sin_approx(1.6)