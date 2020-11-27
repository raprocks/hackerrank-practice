import numpy
numpy.set_printoptions(sign=' ')

n,m = map(int, input().split())

print(numpy.eye(n, m, dtype=float))
