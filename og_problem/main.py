import random


def estimate_pi(n):
    num_points_circle = 0
    num_points_square = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_of_point = x ** 2 + y ** 2
        if distance_of_point < 1:
            num_points_circle += 1
        num_points_square += 1

    pi = 4 * (num_points_circle / num_points_square)
    return pi


print(estimate_pi(1000))
