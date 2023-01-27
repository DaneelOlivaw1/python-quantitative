import numpy

a = numpy.zeros((4,4))
# print(a)

for i in range(4):
    for j in range(4):
        a[i][j] = 1 / (i + j + 1)

print(a)