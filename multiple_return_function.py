def is_perfect_square(n):
    f = 1
    while f * f < n:
        f += 1
    return f, f * f == n


def generate_perfect_square(low, high):
    for i in range(LO, HI):
        number, status = is_perfect_square(i)
        if status:
            print("{0:8}".format(i), " is perfect square with number as ", number)


print("Hello {0!r} and {1!s}".format('foo', 'bin'))
LO = int(input("Enter start number : "))
HI = int(input("Enter end :"))
generate_perfect_square(LO, HI)
