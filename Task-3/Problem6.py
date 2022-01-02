import string
#taking a four digit number from user
def  routine(n,counter):
    counter+=1
    numberArr=list(n) 
    #adding zeros to fit it to a 4-digit number
    while len(numberArr)<4:
        numberArr.append('0')
    #check if all array numbers are equal
    isSameNum=True
    for i in numberArr:
        if numberArr[0] !=i:
            isSameNum=False
    if isSameNum :
        print('invalid number')
        return 0
        
    # arranging the list in assending order and setting it into int
    numberArr.sort()
    assending = ''.join([elem for elem in numberArr])
    assending=int(assending)
    # arranging the list in dessending order and setting it into string
    numberArr.sort(reverse=True)
    dessending = ''.join([elem for elem in numberArr])
    dessending=int(dessending)
    # subtract the smaller number from the bigger number and check if it is equal 6174
    if dessending-assending != 6174:
        routine(str(dessending-assending),counter)
    else:
        print(counter)
       
n=input('Enter 4 digit number: ')
routine(n,0)

