def multiple_3_5(number):
    if number % 3 == 0 or number % 5 == 0:
        return number
    else:
        return 0


def find_sum(limit):
    sum = 0
    for i in range(0, limit):
        sum += multiple_3_5(i)
    print("Sum is {}".format(sum))


limit = int(input("Enter max : "))
find_sum(limit)
