import numpy as np

#my_array = np.array([10, 20, 30, 40, 50 , 60, 70, 80, 90, 100], ndmin = 2)
#print(my_array)
#print(type(my_array))
#print(my_array.shape)
#print(my_array.ndim)
#
#
#array_empty = np.empty((10, 0))
#print(array_empty)
#
#
#array_ones = np.ones((10))
#array_zeros = np.zeros((10))
#print(array_ones)
#print(array_zeros)
#
#array_zeros = np.insert(array_zeros, 3, 1001)
#print(array_zeros)
#
#array_zeros = np.append(array_zeros, 25)
#print(array_zeros)
#
#
#
#random_array = np.full((10), 99)
#
#print(random_array)



#import matplotlib.pyplot as plt
#
#
#x = np.linspace(-np.pi, np.pi, 1000)
#plt.plot(x, np.exp(x))
#plt.show()	













#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#
## Generate some sample data
#x = np.linspace(-5, 5, 100)
#y = np.linspace(-5, 5, 100)
#x, y = np.meshgrid(x, y)
#z = (x**2 + y**2)
#
## Create a 3D plot
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
## Plot the surface
#surf = ax.plot_surface(x, y, z, cmap='viridis')
#
## Add labels and title
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#ax.set_title('3D Plot')
#
## Add a color bar which maps values to colors
#fig.colorbar(surf)
#
## Show the plot
#plt.show()


a = np.array([[1, 2],
              [3, 4]])

print(a.shape)
