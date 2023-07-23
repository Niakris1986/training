from random import random

avg_size = 10
scores = []
values = [0] * avg_size
ptr = 0
mx_range = 32000


def get_previous(index):
    return values[(index - 1) % avg_size]


def get_avg():
    avg = sum(values)/ len(values)
    return avg


for i in range(mx_range):
    values[int(ptr)] = get_previous(ptr) + random() * 2 - 1
    ptr = (ptr + 1) % avg_size
    if i > avg_size:
        print(i, '\t', get_avg())

    # print(i, values)


