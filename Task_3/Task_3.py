import numpy as np
import matplotlib.pyplot as plt
import random

'''
Task 3
Визуализируйте random walk в 2-мерном пространстве, где вы начинаете в (0, 0) и можете 
перемещаться вверх, вниз, вправо и влево. Как визуализировать - скаттерплот, где по x - x, а по y - y
'''

coordinates = np.zeros(2)
steps = 101
path = np.array([])

for idx, step in enumerate(range(steps)):
    movement = random.choice([[1, 0], [0, 1], [-1, 0], [0, -1]])
    coordinates += np.array(movement)
    plt.scatter(coordinates[0], coordinates[1], marker='.')
    plt.text(coordinates[0], coordinates[1], str(idx), fontsize=9, alpha=0.5)

plt.title("Random walk")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
