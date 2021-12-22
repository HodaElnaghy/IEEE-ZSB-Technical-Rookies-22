#Function printing the second maximum number in the array
def SecondMax(arr,Length):
    arr.sort()
    print(arr[Length-2])

#Function printing the second maximum number in the array
def secondMax (arr):
    max=0
    second=0
    for i in range(len(arr)):
        #if the integer in the array more than the max

        if arr[i] > max:
            #put the max value in the "second"variable
            second = max
            #put this number in the max
            max = arr[i]
        #also check on the terms that are less than max as the max can be the first term
        elif arr[i]>second:
            second=arr[i]
    print(second)

def SecondMax(arr,Length):
    arr.sort()
    print(arr[Length-2])

InPut =[]
Length= 0
#Condition to make sure that the length of the array is between 2,10
while Length >10 or Length<2:
    #Splitting the input and putting it into list
    Length = int(input('Enter length of the array'))
    #Taking the input array from the user
    s=input('enter the array')
    arr=(s.split())
    #Converting the input from string to integer
    if len(arr)!=Length:
        Length=0
    for i in range(len(arr)):
        arr[i]=int(arr[i])
        #Condition to make sure array[i] doesn't exceed the limit
        if arr[i] >100 or arr[i]<-100 :
            Length = 0

#Calling second maximum number function
secondMax(arr)
SecondMax(arr,Length)




