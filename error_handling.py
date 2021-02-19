import sys


def convert_string_to_number(slist: list) -> int:
    d: dict = {
        "One": 1, "Two": 2
    }
    number: str = ''
    try:
        for s in slist:
            number += str(d[s])
        return number
    except (KeyError, TypeError) as e:
        print(f'error ==> {e!r}', file=sys.stderr)
        raise
    finally:
        print('FInally block always executed')



print(convert_string_to_number("One T1wo".split()))