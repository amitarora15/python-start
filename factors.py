def factors(n: int) -> list:
    f: list = []
    r: int = 2
    while n >= 2:
        if n % r == 0:
            f.append(r)
            n //= r
        else:
            r += 1
    return f


print(f'26 factors: {factors(600851475143)}')
