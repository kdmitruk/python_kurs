import math
import random


def approximate_pi():
    times = 1000000

    counter = 0

    for _ in range(times):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if math.sqrt(x**2+y**2)<=1:
            counter += 1

    return 4*(counter/times)

