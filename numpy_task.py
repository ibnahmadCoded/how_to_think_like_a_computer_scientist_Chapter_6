import numpy as np

a = np.array([230, 10, 284, 39, 76])

cutoff = 100

b = a[a <= cutoff]

while len(b) > 0:
    a[a <= cutoff] = a[a <= cutoff] * 2
    b = a[a <= cutoff]

print(a)
