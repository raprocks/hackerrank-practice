import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(list(map(float, input().split())))

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
