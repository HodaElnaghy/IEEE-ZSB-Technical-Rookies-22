def secondLowest (records,N):
    min=0
    second =1
    third =0

    for i in range(N):
        # if the integer in the array less than the min

        if records[i][1] <= records[min][1]:
            third = second
            # put min value in the "second"variable
            second = min

            # put this number in the min
            min = i
        # also check on the terms that are less than max as the max can be the first term
        elif records[i][1] <= records[second][1]:
            third = second
            second = i
        elif records[i][1] <= records[third][1]:
            third = i


    arr =[records[second][0],records[third][0]]
    arr.sort()
    print(arr[0])
    print(arr[1])









records = []
names=0
grades=1
N=0
while N <2 or N>5:
    N=int(input("Enter number of students: "))

for i in range (N):
    records.append([])
    records[i].append(input())
    records[i].append(int(input()))

print(records)
secondLowest(records,N)

