#initiating array for number of element in array, number of rotations and number of queries
arr_n_k_q=[]
n=0
k=0
q=0
condition1=True
while condition1:
    #putting the input in an array and converting it to integers
    s = input("Enter N, k and q ")
    arr_input1 = (s.split())
    for i in range (3):
        arr_n_k_q.append(int(arr_input1[i]))
    n = arr_n_k_q[0]
    k= arr_n_k_q[1]
    q=arr_n_k_q[2]
    #checking fo constrains
    if (n>0 and n<=1000000):
        if(k >0 and k<=100000):
            if(q>0 and q<=500):
                break
arr=[]

#taking the array elements from input function and converting it to integers
while condition1:
    x=0
    s1 = input("Enter array: ")
    arr1 = (s1.split())
    for i in range (n):
        arr.append(int(arr1[i]))
        if (arr[i]>=0 and arr[i]<=100000):
            x+=1
    if (x==n):
        break

#taking the indices required to print after array rotation from the user
queries=[]
while condition1:
    y=0

    for i in range (q):
        s2 = input("Enter queries: ")
        queries.append(int(s2))
        #checking for constrains
        if (queries[i]>=0 and queries[i]<n):
            y+=1
    if (y==q):
        break

temp=0
for j in range (k):
    temp =arr[n-1]
    for i in range(n-1,-1,-1):
        if(i==0):
            arr[0]=temp
        else:
            arr[i]=arr[i-1]


for i in range (q):
    print(arr[queries[i]])


