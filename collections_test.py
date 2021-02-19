import collections


def calculate_fre(s: str, number: list = [1,2,3,41,1,3]):
    fq = collections.Counter(s.lower())
    print(fq)
    print(fq.most_common(2))

    fq1 = collections.Counter(number)
    fq1.update()
    print(fq1)
    print(fq1.most_common(2))


calculate_fre("This is true lazy fox")
