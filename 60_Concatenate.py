import numpy

n, m, p = map(int, input().split())

A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((A, B), axis=0))
