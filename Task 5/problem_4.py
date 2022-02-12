def BeutifulTpriplets(arr,n,d):
    counter=0
    c=0
    temp1=0
    temp2=0
    for i in range(len(arr)):
        c=0
        temp1=arr[i]+d
        temp2=arr[i]+2*d
        for j in range (i,n):
            if (arr[j]==temp1):
                c+=1
            if (arr[j]==temp2):
                c+=1
        if (c>=2):
            counter+=1
    print(counter)





d=0
n=0
condition1=True
arr_n_d=[]
while condition1:
    #putting the input in an array and converting it to integers
    s = input("Enter number of elements of array and diffrence: ")
    arr_input1 = (s.split())
    for i in range (2):
        arr_n_d.append(int(arr_input1[i]))
    n = arr_n_d[0]
    d= arr_n_d[1]

    #checking fo constrains
    if (n>0 and n<=10000):
        if(d >0 and d<=20):
            break
arr=[]
arrSorted=[]
while condition1:
    x=0
    arr=[]
    s1 = input("Enter array: ")
    arr1 = (s1.split())
    for i in range (n):
        arr.append(int(arr1[i]))
        if (arr[i]>=0 and arr[i]<=20000):
            x+=1


    if (x==n and arr==sorted(arr)):
        break


BeutifulTpriplets(arr,n,d)