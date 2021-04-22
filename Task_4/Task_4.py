import numpy as np
import matplotlib.pyplot as plt
from random import randint


'''
Task 4
Сгенерируйте и нарисуйте треугольник Серпинского (https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle); 
hint (https://www.youtube.com/watch?v=8ZSlT70pU7A&feature=emb_logo)
'''


def half_dist(p, q):
    return [0.5 * (p[0] + q[0]), 0.5 * (p[1] + q[1])]


corner = [(0, 0), (0.5, 0.5), (1, 0)]

points = 10000
x = np.zeros(points)
y = np.zeros(points)

for i in range(1, points):
    vertex = randint(0, 2)
    x[i], y[i] = half_dist(corner[vertex], (x[i - 1], y[i - 1]))

plt.scatter(x, y, s=3)
plt.title("Sierpiński triangle")
plt.show()
