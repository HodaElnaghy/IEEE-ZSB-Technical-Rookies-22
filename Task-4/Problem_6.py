def chocolateFeast(n,c,m):
    choco=count=int(n/c)
    while choco > 1 and choco>=m :
        ret=int(choco/m)
        count+=ret
        choco= choco%m +ret
    return count


if __name__ == '__main__':
    t = int (input("Enter the no. of test cases: "))
    for i in range (t):
        n,c,m = map(int, input().split())
        print (chocolateFeast(n,c,m))