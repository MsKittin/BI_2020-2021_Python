import numpy as np
import random
import matplotlib.pyplot as plt
import time


'''
Task 1.
Замерьте время вычисления чисел от 0 до 1 из равномерного распределения с помощью модуля random и модуля numpy, 
изобразите зависимость времени вычисления от количества вычисляемых чисел для них. Другими словами - 
по x идёт то, сколько чисел за прогон вы взяли от 0 до 1, а по y - время, которое это заняло. 
Сравните время выполнения в numpy и в random.
'''

# numpy.random solution

elapsed_list_numpy = []

for i in range(1, 1001):

    start_time = time.time()
    np.random.uniform(0, 1, i)
    elapsed_list_numpy.append(time.time() - start_time)

plt.figure(figsize=(15, 10))
plt.scatter(range(1, 1001), elapsed_list_numpy)

plt.title("Numpy solution")
plt.xlabel("amount of calculated numbers")
plt.ylabel("computation time")
plt.show()

print('numpy.random solution mean time:', np.mean(elapsed_list_numpy))


# random solution

elapsed_list_random = []

for i in range(1, 1001):
    time_start = time.time()
    for j in range(1, i + 1):
        random.uniform(0, 1)
    elapsed_list_random.append(time.time() - time_start)

plt.figure(figsize=(15, 10))
plt.scatter(range(1, 1001), elapsed_list_random)

plt.title("Random solution")
plt.xlabel("amount of calculated numbers")
plt.ylabel("computation time")
plt.show()

print('random mean solution time:', np.mean(elapsed_list_random))

'''
numpy.random solution is faster. In this case it's better to use numpy module, because loops make program slower.
'''
