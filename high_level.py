import math

PI = 3.14159265359
EPS = 1e-10

n = 0
a = ((-1) ** n * (PI / 2) ** (2 * n)) / ((math.factorial(2 * n)) * (4 * n + 1))
sum = 0.0
while math.fabs(a) > EPS:
    a = ((-1) ** n * (PI / 2) ** (2 * n)) / ((math.factorial(2 * n)) * (4 * n + 1))
    sum += a
    n += 1
print(sum)