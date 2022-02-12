def kaprekarNumbers(p, q):
    kap = []
    for n in range(p, q + 1):
        right = []
        left = []
        sq = str(n * n)
        d = len(str(n))
        if len(sq) % 2 == 0:
            for i in range(d):
                left.append(sq[i])
            for i in range(d, len(sq)):
                right.append(sq[i])
        else:
            for i in range(d - 1):
                left.append(sq[i])
            for i in range(d - 1, len(sq)):
                right.append(sq[i])
        l = "".join(left)
        r = "".join(right)
        if l == '':
            l = 0
        else:
            l = int(l)
        r = int(r)
        if l + r == n:
            kap.append(n)
    if len(kap) == 0:
        print("INVALID RANGE")
    else:
        print(*kap, sep=" ")


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)

