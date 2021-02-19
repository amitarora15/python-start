k = int(input("Enter input : "))
print(k, end = ' ')
if k < 0:
    print("Invalid input")
else:
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        print(k, end=' ')
