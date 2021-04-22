import numpy as np
import matplotlib.pyplot as plt


'''
Task 6
Сгенерируйте и нарисуйте коврик Серпинского (https://en.wikipedia.org/wiki/Sierpinski_carpet)
'''

total_times = 5


def sierpinski_carpet(total):
    m = np.array([[0]])

    for x in range(1, total + 1):
        concatenate = np.concatenate((m, m, m), axis=1)
        m = np.concatenate((concatenate,
                            np.concatenate((m, np.ones([3 ** (x - 1), 3 ** (x - 1)]), m), axis=1),
                            concatenate), axis=0)
    return m


plt.spy(sierpinski_carpet(total_times))  # visualize non-zero values
plt.title("Sierpiński carpet")
plt.show()
