import numpy

lis = input().split()

my_array = numpy.array([*map(int, lis)])
print(numpy.reshape(my_array, (3, 3)))
