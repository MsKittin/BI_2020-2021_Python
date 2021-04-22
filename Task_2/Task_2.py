import numpy as np
import matplotlib.pyplot as plt
import time


'''
Task 2
Сделайте функцию для проверки является ли список отсортированным (без использования sorted или sort). 
Затем реализуйте monkey sort (https://en.wikipedia.org/wiki/Bogosort), а потом визуализируйте следующее: 
распределение времени работы алгоритма от размера сортируемого списка. То есть по x идёт размер массива, 
а по y - среднее время нескольких прогонов и их отклонение (или дисперсия)
'''


def is_sorted(lst):  # test if list is sorted
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def shuffle(lst):  # random shuffle elements in list
    lst_length = len(lst)
    for i in range(lst_length):
        r = np.random.randint(0, lst_length)
        lst[i], lst[r] = lst[r], lst[i]
        return lst


def monkey_sort(lst):
    while not is_sorted(lst):
        shuffle(lst)


for i in range(1, 7):
    time_list = []
    for j in range(1, 4):
        cur_list = np.random.randint(1, 100, i)
        start_time = time.time()

        monkey_sort(cur_list)
        finish_time = time.time()

        cur_time = finish_time - start_time
        time_list.append(cur_time)
    time_std = np.std(time_list)
    plt.bar(i, np.mean(time_list), yerr=time_std)

plt.title("Dependence of execution time on list length")
plt.xlabel("list length")
plt.ylabel("mean time")
plt.show()
