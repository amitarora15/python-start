a = 0
print('while looping starts')
while a < 10:
    print(a, end = ' ')
    a += 1
else:
    print("Loop ends")

a = 0
print('while looping with break starts')
while a < 10:
    print(a, end = ' ')
    a += 1
    if a == 5:
        break
else:
    print("Loop ends")

print('\nfor looping starts')
i = 0
for i in range(10):
    print(i, end=' ')
    i += 1
else:
    print("Loop ends")



# x = ['ab', 'cd']
# for i in x:
#     x.append(i.upper())
#     print(x)

