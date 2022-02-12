def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = [(d1-d2)*15,(m1-m2)*500,(y1-y2)*10000]
    if sum(fine)<=0:
        return 0
    return max(fine)

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
print (libraryFine(d1,m1,y1,d2,m2,y2))