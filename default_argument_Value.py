def printItems(m=[]):
    if m is None:
        m = []
    m.append('spam')
    return m


print(printItems())
print(printItems())