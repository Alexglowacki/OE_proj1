import math


def f_rana(point):
    s = 0.0
    array = []
    for i in range(len(point) - 1):
        p1 = point[i] * math.cos(math.sqrt(abs(point[i + 1] + point[i] + 1.0)))
        p2 = math.sin(math.sqrt(abs(point[i + 1] - point[i] + 1.0)))
        p3 = (1.0 + point[i + 1]) * math.sin(math.sqrt(abs(point[i + 1] + point[i] + 1.0)))
        p4 = math.cos(math.sqrt(abs(point[i + 1] - point[i] + 1.0)))
        s += p1 * p2 + p3 * p4
        array.append(s)
    return array

