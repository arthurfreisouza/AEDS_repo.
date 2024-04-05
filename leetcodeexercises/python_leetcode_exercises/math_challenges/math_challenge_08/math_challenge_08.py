import numpy as np
def Pythagorean_Function():
    for a in range(500):
        for b in range(500):
            c = np.sqrt(pow(a, 2) + pow(b, 2))
            if (c > b) & (b > a) & (a + b + c == 1000):
                print()
                print(' The product of {} x {} x {} is : {}'.format(a, b, c, a * b * c))

Pythagorean_Function()
 