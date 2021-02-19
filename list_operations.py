def list_opr(l: list):
    l.append(12)
    l.append("Amit")
    l.append([1, 2, 3])
    l.insert(34, 5)
    print(l)
    print(l.index("Amit"))
    #print(l.index(32))
    print(l.count(12))
    l.extend([1, 2, 3])
    print(l)
    l.reverse()
    print(l)
    #l.sort()
    print(l)
    l_new: list = l[::-1]
    print(l_new)
    l_new[0] = 'Amit'
    print(l_new)
    print(l)


mylist: list = []
list_opr(mylist)