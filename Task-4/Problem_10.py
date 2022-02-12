def getMoneySpent(keyboards, drives, b):
    max=-1
    for x in keyboards:
        for y in drives:
            if x+y>max and x+y<=b:
                max=x+y
    return max
if __name__ == '__main__':
    b, n, m = map(int, input().split())
    keyboards = list(map(int,input().strip().split()))[:n]
    drives = list(map(int,input().strip().split()))[:m]
    print(getMoneySpent(keyboards, drives, b))

    