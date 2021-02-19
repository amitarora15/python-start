out = open("new_reader.txt", "w")

for l in open("reader.txt"):
    print(l.strip())
    #out.write(l)
    print(l, file=out)
out.close()

