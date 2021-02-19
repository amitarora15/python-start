def is_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True


print(is_prime(2))
print(is_prime(25))
