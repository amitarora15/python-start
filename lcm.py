import math
from functools import reduce


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


lcm2 = 1
for i in range(1, 21):
    lcm2 = lcm(lcm2, i)
print(lcm2)


def lcmr(many: list) -> int:
    if len(many) == 1:
        return many[0]
    if len(many) == 2:
        return lcm(many[0], many[1])
    return lcm(lcm(many[0], many[1]), lcmr(many[2:]))


print(lcmr(range(1,21)))


def lcmf(many):
    return reduce(lcm, many)


print(lcmf(range(1, 21)))