def take(count: int, iterable: list):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        print(f'taking item {item}')
        counter += 1
        yield item


def distinct(iterable: list):
    seen = set()
    for item in iterable:
        print(f'distinct item {item}')
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    """Taking three distinct items
    from the list"""
    s = [3, 6, 6, 2, 1, 1]
    for i in take(3, (distinct(s))):       #lazy evaluation make only some part to be processed, if you need to verify the logic pass list(distinct(s) -- then will work for all
        print(i, end=" ")


run_pipeline()