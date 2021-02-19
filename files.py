import sys

print(sys.getdefaultencoding())

f = open('new_file.txt', mode='wt')
f.write('Hello my name')
f.write(' is Amit Arora\n')
f.write('I am 39 years old')
f.close()

f = open('new_file.txt', mode='rt', encoding='utf-8')
print(f.read())
f.seek(0)
print('lines ')
print(f.readline())

f.seek(0)
print(f.readlines())
f.close()

f = open('new_file.txt', mode='at', encoding='utf-8')
print(f.writelines(
                   [
                       '\nI am new\n',
                        'I will win'
                    ]
))
f.close()

f = open('new_file.txt', mode='rt', encoding='utf-8')
for line in f:
    print(line)
f.close()
