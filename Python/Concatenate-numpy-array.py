import numpy

m, n, p = map(int, input().split())
columns = []
for _ in range(m):
    column = map(int, input().split())
    columns.append(list(column))

array1 = numpy.array(columns)
columns = []

for _ in range(n):
    column = map(int, input().split())
    columns.append(list(column))

array2 = numpy.array(columns)

print(numpy.concatenate((array1, array2)))
