Test_cases=-1
n=0
a=0
b=0
nu=0
while (Test_cases <0 or Test_cases>10):
    Test_cases= int(input("Enter number of test cases: "))
list1=[]
stone=0
list2=[]
list2.append(0)
for i in range (Test_cases):
    nu=0
    n = 0
    a = 0
    b = 0
    while(n<=1 or n>=1000):
        n=int(input("Enter numbers of stones: "))
    while (a < 1 or a > 1000):
        a = int(input("Enter the diffrence between the stones: "))
    while (b < 1 or b > 1000):
        b = int(input("Enter the diffrence between the stones: "))


    for i in range (n):
        stone = 0
        for x in range (i):

            stone+=a
        for j in range(n-1-i):
            stone+=b
        list1.append(stone)
    list1=sorted(set(list1))
    nu=len(list1)
    list2.append(nu)

for i in range (Test_cases):
    list3 = []
    for j in range(list2[i],list2[i+1]):
        list3.append(list1[j])

    print(list3)
