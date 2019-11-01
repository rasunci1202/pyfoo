import numpy
import numpy.random
import matplotlib.pyplot as plt

#
# TEST: heatmap, extents
#
"""
my_x_list = numpy.random.randn(1, 8)
my_y_list = numpy.random.randn(1, 8)
my_z_list = numpy.random.randn(8, 1)

print(my_x_list)
print(my_x_list.shape)
my_tx_list = my_x_list.transpose()
print(my_tx_list)
print(my_z_list)

my_x_list = numpy.random.randn(2048)
my_y_list = numpy.random.randn(2048)
my_heatmap, my_x_edges, my_y_edges = numpy.histogram2d(my_x_list, my_y_list, bins=(64,64))
my_extent = [my_x_edges[0], my_x_edges[-1], my_y_edges[0], my_y_edges[-1]]

plt.clf()
plt.title('Pythonspot.com heatmap example')
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(my_heatmap, extent=my_extent, origin='lower')
plt.show()
"""

#
# TEST: histogram, hist
#
#my_x_list = numpy.asarray([0] * 64)
#my_x_list = numpy.random.randint(25, 75, size=64)
"""
my_x_list = numpy.array(
    [20, 22, 23, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     90, 91, 92, 100]
    )
"""
"""
my_y_list = numpy.asarray([1] * 64)
#my_bin_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_x_list = numpy.array([10, 11, 12, 13, 55, 45, 33, 54, 90, 18, 77, 49, 39])
my_bin_list = [0, 20, 40, 60, 80, 100]

print(my_x_list)
print(my_x_list.shape)
print(my_y_list)
print(my_y_list.shape)

numpy.histogram(my_x_list, my_bin_list)
my_histogram, my_bins = numpy.histogram(my_x_list, my_bin_list)
print(my_histogram)
print(my_bins)
plt.hist(my_x_list, bins=my_bins, density=False)
plt.show()
plt.hist(my_bins[:-1], my_bins, weights=my_histogram)
plt.show()
"""

#
# TEST: histogram2d, hist2d
#
my_x_list = numpy.asarray([51] * 128)
print(my_x_list)
print(my_x_list.shape)
my_y_list = numpy.asarray([50] * 128)
print(my_y_list)
print(my_y_list.shape)
my_changes = numpy.asarray([42, 43, 44, 25, 28, 29])
my_changes_reversed = my_changes[::-1]
print(my_changes_reversed)
my_x_list[40:46] = my_changes
my_x_list[50:56] = my_changes[::-1]
my_x_list[0:40] = numpy.asarray([19] * 40)
my_y_list[70:76] = my_changes
my_y_list[80:86] = my_changes[::-1]
my_y_list[0:40] = numpy.asarray([18] * 40)
print(my_x_list)
print(my_y_list)
my_bin_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist2d(my_x_list, my_y_list, bins=my_bin_list)
plt.show()
my_histogram2d, my_x_bins, my_y_bins = numpy.histogram2d(my_x_list, my_y_list, bins=my_bin_list)
plt.hist2d(my_x_bins, my_y_bins, weights=my_histogram2d)
plt.show()


