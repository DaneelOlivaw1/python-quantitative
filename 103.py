import math
import matplotlib.pyplot as plt

def target_func(x):
    return math.cos(x)

def draw_func(func, x_rage, pieces):
    step = (x_rage[1] - x_rage[0]) / pieces
    xs = []
    ys = []
    for i in range(pieces):
        x = i * step
        y = func(x)
        xs.append(x)
        ys.append(y)
    
    plt.plot(xs,ys)
    plt.show()

draw_func(target_func, (0, 2 * 3.14), 1000)


