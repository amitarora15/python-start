def is_armstrong(number):
    sum = 0
    org_number = number
    while number > 0:
        #n = number % 10
        number, n = divmod(number, 10)
        sum += (n ** 3)
        #number //= 10
    if sum == org_number:
        print("{my} number is armstrong number".format(my=org_number))
    #else:
     #   print("{my} number is not armstrong number".format(my=org_number))


num = int(input("Enter number : "))
is_armstrong(num)

for i in range(100, 1000):
    is_armstrong(i)

