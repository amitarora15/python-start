def fib(n: int) -> list:
    a, b = 0, 1
    f: list = []
    for a in range(n):
        f.append(a)
        a, b = b, a + b
    return f


def fib_with_yield(n: int) -> list:
    a, b = 0, 1
    for a in range(n):
        yield a
        a, b = b, a + b


print(fib(10))
print(sum([x for x in fib(4000000) if x % 2 == 0]))

print(sum([x for x in fib_with_yield(4000000) if x % 2 == 0]))


