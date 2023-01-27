import numpy


l1 = [0.5, 1.43, -1.36, -0.16, 0.29, -0.59, 1.16,-0.33, 0.07, -1.36]
l2 = [1, 2, 4, 5, 9999]
l = numpy.array(l2)

print(f"均值:{l.mean()}")
print(f"方差:{l.var()}")
print(f"标准差:{l.std()}")
print(f"中位数:{numpy.median(l)}")
