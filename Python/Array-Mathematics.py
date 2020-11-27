import numpy
'''
Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )
'''

N, M = map(int, input().split())

arrayA = numpy.array([list(map(int, input().split())) for n in range(N)])
arrayB = numpy.array([list(map(int, input().split())) for n in range(N)])


print(arrayA + arrayB)
print(arrayA - arrayB)
print(arrayA * arrayB)
print(arrayA // arrayB)
print(arrayA % arrayB)
print(arrayA ** arrayB)

