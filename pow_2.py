import math


def smallest_pow_of_two(n):
    total = 0
    while n > 0:
        t = 0
        while math.pow(2, t) < n:
            t += 1
        if math.fabs(n-math.pow(2, t)) < math.fabs(n-math.pow(2, t-1)):
            close = t
        else:
            close = t-1
        total += 1
        print close
        n = math.fabs(n-math.pow(2, close))
    return total



print smallest_pow_of_two(29)