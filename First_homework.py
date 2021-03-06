import numpy as np

# Task 1

# Посчитайте абсолютную разницу между суммой квадратов смежных элементов и суммой квадратов смежных чисел в эррее для эррея с числами подряд от 1 до 1000
# Пример для чисел от 1 до 3
# [1 2 3]
# abs((1 **  2 + 2 **  2) - (1 + 2) **  2) == 4
# abs((2 **  2 + 3 **  2) - (2 + 3)  ** 2) == 12
# [4 12]

arr1 = np.arange(1, 1001)
squared_arr1 = arr1 ** 2

print(abs((squared_arr1[::2] + squared_arr1[1::2]) - (arr1[::2] + arr1[1::2]) ** 2))


# Task 2

# Посчитайте сумму чисел, обратных к числам от 1 до n. 
# Пример для 3
# 1 + 1/2 + 1/3 == 1.8(3)

n = int(input())

arr2 = np.arange(1, n + 1)
rev_arr2 = 1 / arr2
print(rev_arr2.sum())


# Task 3

# Посчитайте сумму чётных чисел Фибоначчи из первых 125 чисел Фибоначчи

n = 125

F = np.array([[0, 1], [1, 1]], dtype=float)
needed_indices = np.arange(1, n + 1)
fib_numbers = np.array([], dtype=float)

for i in needed_indices:
    fib_number = np.linalg.matrix_power(F, i - 1)[0, 1]
    if fib_number % 2 == 0:
        fib_numbers = np.concatenate((fib_numbers, np.array([fib_number])))

print(fib_numbers.sum())


# Task 4

# Сделайте лог случайных перемещений в 2д пространстве
# Начинаем в начале координат 0, 0
# Каждый ход случайно перемещаемся на нормально распределённую случайную величину вправо или влево и вверх или вниз
# Вероятность перемещения вверх или вниз и вправо или влево равновероятная (4 варианта)
# Функция должна принимать число шагов, которое мы идём, принтить перемещение на каждом шаге и возвращать список с координатами на каждом шаге

coordinates = np.zeros(2)
steps = int(input())

print('Start from:',  coordinates)
for step in range(steps):
    move = np.array(np.random.normal(size=2))
    x_move = round(move[0], 2)
    y_move = round(move[1], 2)
    print('Moved {} by x-axis and {} by y-axis'.format(str(x_move), str(y_move)))
    coordinates = coordinates + np.array([x_move, y_move])
    print('Coordinates now are {}\n'.format(str(coordinates)))
