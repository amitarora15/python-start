def reverse(n: int, d: int) -> int:
    if d == 1 or n == 0:
        return n
    div, mod = divmod(n, 10)
    return mod * 10 ** (d - 1) + reverse(div, d-1)


def is_palindrome(n: int) -> bool:
    return n == reverse(n, len(str(n)))


print(is_palindrome(1234))
print(is_palindrome(123321))
print('.'.join(['A','m','i','t']))
