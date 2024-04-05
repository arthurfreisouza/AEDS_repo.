import matplotlib.pyplot as plt
import numpy as np
def linear_function(x):
    return x + 5

x = np.linspace(0, 10, 100)
y1 = linear_function(x)
y2 = linear_function(x)
y3 = linear_function(x)
y4 = linear_function(x)
y5 = linear_function(x)
y6 = linear_function(x)
y7 = linear_function(x)
y8 = linear_function(x)
fig1, axis1 = plt.subplots(nrows = 4, ncols = 4)


axis1[0,0].plot(x, y1)
axis1[0,1].plot(x, y2)
axis1[1,0].plot(x, y3)
axis1[1,1].plot(x, y4)
axis1[1,2].plot(x, y5)
axis1[2,1].plot(x, y6)
axis1[2,2].plot(x, y7)
plt.show()
fig1.savefig('/home/arthur/Desktop/savefig.png')

plt.scatter()
