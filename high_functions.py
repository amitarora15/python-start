import math


def select(n):
    return n % 3 == 0 or n % 5 == 0


def square(x):
    return x * x


print(sum(filter(select, range(1000))))
print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))

print(list(map(square, range(10))))

f = [1,2,3]
p = [4,5,6]
print(list(zip(f, p)))

print(list([x for x in range(10) if select(x)]))
print(list([x * x for x in range(10) if x % 3 == 0]))
print(list([x for x in range(10)]))
print(list([x*x for x in range(10)]))

