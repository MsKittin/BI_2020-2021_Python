import numpy as np
import matplotlib.pyplot as plt

# Заимплементируйте хаотическую симуляцию с лекции и выясните:


def round_computations(n, r):
    return n * r * (1 - n)


# Task 1

# зависимость численности популяции во все временные шаги от r - прогоняем обычную симуляцию с одним r, получаем эррей
# с численностями, плоттим его на картинке как скаттерплот, где численности это y, а r это x, повторяем со следующим r

# rs взяты до 4, потому что при 5 график непоказательный

n_0 = 0.3
rs = np.arange(0, 4, 0.1)
t = np.arange(10000)
ns = np.zeros(t.size)


for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0

    for time in t[1:]:
        ns[time] = round_computations(ns[time - 1], r)

    plt.scatter(np.full(t.size, r), ns, s=1.5)
    plt.title("Численность во все временные шаги")
    plt.xlabel("r")
    plt.ylabel("N")

plt.show()


# Task 2

# то же самое, но теперь берите не все численности популяции, а только численности, после 1000 шага

n_0 = 0.3
rs = np.arange(0, 5, 0.1)
t = np.arange(10000)
ns = np.zeros(t.size)


for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0

    for time in t[1:]:
        ns[time] = round_computations(ns[time - 1], r)

    ns = ns[1001:]
    plt.scatter(np.full(ns.size, r), ns, s=1.5)
    plt.title("Численности после 1000 шага")
    plt.xlabel("r")
    plt.ylabel("N")

plt.show()


# Task 3

# в предыдущем графике зазумьтесь в область от 3.5 до конца. зазумьтесь ещё 2 раза в более
# маленькие интервалы внутри этого

# зумлюсь первый раз

n_0 = 0.3
rs = np.arange(0, 5, 0.01)
t = np.arange(10000)
ns = np.zeros(t.size)

for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0

    for time in t[1:]:
        ns[time] = round_computations(ns[time - 1], r)

    ns = ns[1001:]

    plt.scatter(np.full(ns.size, r), ns, s=1.5)
    plt.axis([3.5, 4, 0, 1])
    plt.title("Зум в (3.5, 4) по иксу")
    plt.xlabel("r")
    plt.ylabel("N")

plt.show()


# зумлюсь поближе в левую часть

n_0 = 0.3
rs = np.arange(0, 5, 0.01)
t = np.arange(10000)
ns = np.zeros(t.size)

for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0

    for time in t[1:]:
        ns[time] = round_computations(ns[time - 1], r)

    ns = ns[1001:]

    plt.scatter(np.full(ns.size, r), ns, s=1.5)
    plt.axis([3.5, 3.7, 0, 1])
    plt.title("Зум в (3.5, 3.7) по иксу")
    plt.xlabel("r")
    plt.ylabel("N")

plt.show()


# зумлюсь поближе в правую часть

n_0 = 0.3
rs = np.arange(0, 5, 0.01)
t = np.arange(10000)
ns = np.zeros(t.size)

for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0

    for time in t[1:]:
        ns[time] = round_computations(ns[time - 1], r)

    ns = ns[1001:]

    plt.scatter(np.full(ns.size, r), ns, s=1.5)
    plt.axis([3.7, 3.9, 0, 1])
    plt.title("Зум в (3.7, 3.9) по иксу")
    plt.xlabel("r")
    plt.ylabel("N")

plt.show()
