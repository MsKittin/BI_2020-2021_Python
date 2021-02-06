import numpy as np
import matplotlib.pyplot as plt

'''
Task 4
Сгенерируйте и нарисуйте треугольник Серпинского (https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle); 
hint (https://www.youtube.com/watch?v=8ZSlT70pU7A&feature=emb_logo)
'''

point_a = np.array([0, 150])
point_b = np.array([-200, -150])
point_c = np.array([200, -150])

start_point = [np.random.randint(-80, 80), np.random.randint(-80, 80)]

plt.plot(point_a[0], point_a[1], marker='.', markersize=3)
plt.plot(point_b[0], point_b[1], marker='.', markersize=3)
plt.plot(point_c[0], point_c[1], marker='.', markersize=3)

iterations = 0
last_point = 0

while iterations <= 10000:
    choice = np.random.choice([1, 2, 3])

    if iterations == 0:
        if choice == 1:
            new_point = np.array([((point_a[0] + start_point[0]) / 2), ((point_a[1] + start_point[1]) / 2)])
            plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
            last_point = new_point

        elif choice == 2:
            new_point = np.array([((point_b[0] + start_point[0]) / 2), ((point_b[1] + start_point[1]) / 2)])
            plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
            last_point = new_point

        else:
            new_point = np.array([((point_c[0] + start_point[0]) / 2), ((point_c[1] + start_point[1]) / 2)])
            plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
            last_point = new_point

        iterations += 1
        continue

    if choice == 1:
        new_point = np.array([((point_a[0] + last_point[0]) / 2), ((point_a[1] + last_point[1]) / 2)])
        plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
        last_point = new_point
        iterations += 1

    if choice == 2:
        new_point = np.array([((point_b[0] + last_point[0]) / 2), ((point_b[1] + last_point[1]) / 2)])
        plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
        last_point = new_point
        iterations += 1

    if choice == 3:
        new_point = np.array([((point_c[0] + last_point[0]) / 2), ((point_c[1] + last_point[1]) / 2)])
        plt.plot(new_point[0], new_point[1], marker='.', markersize=3)
        last_point = new_point
        iterations += 1

plt.title("Sierpiński triangle")
plt.show()
