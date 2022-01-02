a = list(map(int,input("Number of elements in each array: ").strip().split()))[:2]
arr1 = list(map(int,input("\nEnter numbers of the first array: ").strip().split()))[:a[0]]
arr2 = list(map(int,input("\nEnter numbers of the first array: ").strip().split()))[:a[1]]
numbers=[]
for i in range (1,max(arr2)+1):
    numbers.append(i)

divisableByFirst = [x for x in numbers if all(x % y == 0 for y in arr1)]
result= [x for x in divisableByFirst if all(y % x == 0 for y in arr2)]
print(f'result= {len(result)} \n')
print(result)