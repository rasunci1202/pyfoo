import numpy
import matplotlib.pyplot as plt
import scipy.stats as sts

my_edge_x = numpy.array([numpy.arange(0,100)])
my_edge_y = numpy.array([numpy.arange(0,100)])
my_grid_x, my_grid_y = numpy.meshgrid(my_edge_x, my_edge_y)
print(my_grid_x)
print(my_grid_y)
my_xs = my_grid_x.ravel()
my_ys = my_grid_y.ravel()
print(my_xs)
print(my_ys)
my_ref_coords = (numpy.vstack([my_xs, my_ys])).T
print(my_ref_coords)


my_data_x = numpy.random.randint(40, 80, size=100)
my_data_y = numpy.random.randint(20, 90, size=100)
print(my_data_x)
print(my_data_y)
my_data = numpy.vstack([my_data_x, my_data_y])
print(my_data)
print(my_data.T)

my_kernel = sts.gaussian_kde(my_data)
print(my_kernel)

my_Z = my_kernel.evaluate(my_ref_coords.T)
print(my_Z)
print(my_Z.shape)
my_reshaped = numpy.reshape(my_Z, my_grid_x.shape)
print(my_reshaped)

pass

"""
my_shape = my_xs.shape
my_trans = my_ref_coords.T
print(my_shape)
print(my_trans)

print(my_xs.shape)
my_foo = my_kernel(my_ref_coords)
print(my_foo)
print(my_foo.shape)
print(my_foo.shape.T)
my_reshaped_kernel = numpy.reshape(my_kernel(my_ref_coords).T, my_xs.shape)
print(my_reshaped_kernel)
"""

my_fig, my_ax = plt.subplots()
my_ax.imshow(numpy.rot90(my_reshaped), extent=[0,4,0,4])
my_ax.plot(my_data_x, my_data_y, 'k.', markersize=2)
my_ax.set_xlim([0,4])
my_ax.set_ylim([0,4])
plt.show()
