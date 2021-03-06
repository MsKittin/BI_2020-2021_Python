import numpy as np
import matplotlib.pyplot as plt

# Task 1

# Создайте эррей с 20 равномерно распределёнными точками от -pi до pi. 
# Затем создайте эррей с синусами этих точек. Нарисуйте график sin(x) от x

x = np.linspace(-np.pi, np.pi, 20)
x_sin = np.sin(x)

x_plot = plt.plot(x_sin, x)
plt.xlabel("x_sin"), plt.ylabel("x")
plt.show()


# Task 2

# Создайте 15 случайных целых чисел от 0 до 100. Создайте переменные evens и odds, которые будут хранить чётные
# и нечётные значения из начального эррея случайных чисел

x = np.random.randint(0, 101, 15)
evens = np.array([])
odds = np.array([])

for num in x:
    if num % 2 == 0:
        evens = np.concatenate((evens, np.array([num])))
    else:
        odds = np.concatenate((odds, np.array([num])))


# Task 3

# Нарисуйте график случайных блужданий - вы начинаете в начале координат (0, 0). 
# Каждый временной шаг вы случайно перемещаетесь на 1 единицу в одном из 4-ёх направление - 
# влево, вправо, вниз, верх (прямо аркадка из прошлого века)). То есть ваши координаты изменяются 
# на (1, 0), (-1, 0), (0, -1) или (0, 1). Заплоттьте 100 шагов, тип графика выберите сами

coordinates = np.zeros(2)
steps = 100
directions = np.array(["up", "down", "right", "left"])
move_log = np.array([])

for step in range(steps):
    direction = np.random.choice(directions)

    if direction == "right":
        coordinates = coordinates + np.array([1, 0])
    elif direction == "left":
        coordinates = coordinates - np.array([1, 0])
    elif direction == "up":
        coordinates = coordinates + np.array([0, 1])
    else:
        coordinates = coordinates - np.array([0, 1])

    move_log = np.concatenate((move_log, coordinates))

    plt.scatter(coordinates[0], coordinates[1])

plt.show()

print(move_log)


# Task 4

# Нарисуйте на одном графике синус и косинус для x от -10 до 10 с шагом 0.1

x = np.arange(-10, 11, step=0.1)
x_sin = np.sin(x)
x_cos = np.cos(x)

plt.plot(x_sin, label='sin(x)')
plt.plot(x_cos, label='cos(x)')
plt.legend()
plt.show()


# Task 5

# Создайте линейный график, построенный по этой формуле P(t) = P0e^(rt) 
# Возьмите P0 = 10, r = 0.8, t от 0 до 30
# Нарисуйте время по оси x, а P оси y

p_0 = 10
r = 0.8
t = np.linspace(0, 30, 100)
p = p_0 * np.e ** (r * t)

plt.plot(t, p)
plt.show()


# Task 6

# Нарисуйте 4 графика на 1-ой картинке (2 строки, 2 колонки)
# y = x^2
# x от 0 до 10 с разными шагами - 0.01, 0.1, 1, 2

y_1 = np.arange(0, 11, step=0.01) ** 2
y_2 = np.arange(0, 11, step=0.1) ** 2
y_3 = np.arange(0, 11, step=1) ** 2
y_4 = np.arange(0, 11, step=2) ** 2

fig = plt.figure()
((plot1, plot2), (plot3, plot4)) = fig.subplots(2, 2)
plot1.plot(y_1)
plot2.plot(y_2)
plot3.plot(y_3)
plot4.plot(y_4)

plt.show()


# Task 7

# Draw functions y = x^2, y = pi  
# Раскрасьте часть параболы, которая больше pi, в другой цвет

x = np.arange(-10, 10, 0.01)
y = x ** 2
y_2 = np.repeat(np.pi, len(x))

y_greater_pi = y[y >= np.pi]
y_less_pi = y[y <= np.pi]

plt.plot(x, y_2)
plt.plot(x[y >= np.pi], y_greater_pi, color="r")
plt.plot(x[y <= np.pi], y_less_pi, color="g")

plt.show()


# Task 8

# Засимулируйте динамику популяции с помощью последнего уравнения с лекции dN/dt = r N (1 - NK)
# И постройте графики для всех комбинаций параметров K и r:
# K > N0
# K < N0
# r < 0
# r = 0
# r > 0
# Добавьте к графикам подписи, легенду, и опишите поведение системы

from scipy import integrate

n_0 = 10
b = 0.8
d = 0.6
r = b - d
k = 1000
t = np.linspace(0, 50, 100)


def complex_malthus(n, t, r, k):
    return r * n * (1 - n / k)


# K > N0, r > 0
population_sizes_1 = integrate.odeint(func=complex_malthus, y0=n_0, t=t, args=(r, k))
plt.plot(t, population_sizes_1, label="K > N0, r > 0")
plt.xlabel("time")
plt.ylabel("population size")
plt.legend()
plt.show()
# быстро возрастает, а потом тормозится у порога capacity

# K > N0, r < 0
n_0 = 10
b = 0.6
d = 0.8
r = b - d
k = 1000
t = np.linspace(0, 50, 100)

population_sizes_2 = integrate.odeint(func=complex_malthus, y0=n_0, t=t, args=(r, k))
plt.plot(t, population_sizes_2, label="K > N0, r < 0")
plt.xlabel("time")
plt.ylabel("population size")
plt.legend()
plt.show()
# убывает, популяция вымирает, т.к. умирает больше, чем рождается

K > N0, r = 0
n_0 = 10
b = 0.8
d = 0.8
r = b - d
k = 1000
t = np.linspace(0, 50, 100)

population_sizes_3 = integrate.odeint(func=complex_malthus, y0=n_0, t=t, args=(r, k))
plt.plot(t, population_sizes_3, label="K > N0, r = 0")
plt.xlabel("time")
plt.ylabel("population size")
plt.legend()
plt.show()
# прямая линия, потому что численность популяции постоянная (умирают и рождаются одинаково)

# K < N0, r > 0
n_0 = 1000
b = 0.8
d = 0.6
r = b - d
k = 100
t = np.linspace(0, 50, 100)

population_sizes_4 = integrate.odeint(func=complex_malthus, y0=n_0, t=t, args=(r, k))
plt.plot(t, population_sizes_4, label="K > N0, r > 0")
plt.xlabel("time")
plt.ylabel("population size")
plt.legend()
plt.show()
# взрыв ядерной бомбы, мгновенная смерть

# K < N0, r < 0
n_0 = 1000
b = 0.6
d = 0.8
r = b - d
k = 100
t = np.linspace(0, 50, 100)

population_sizes_5 = integrate.odeint(func=complex_malthus, y0=n_0, t=t, args=(r, k))
plt.plot(t, population_sizes_5, label="K > N0, r < 0")
plt.xlabel("time")
plt.ylabel("population size")
plt.legend()
plt.show()
# модель не работает

# K < N0, r = 0 так же прямая линия будет
