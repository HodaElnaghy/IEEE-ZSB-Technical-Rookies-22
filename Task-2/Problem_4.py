Function to calculate the shortest distance between 2 numbers
def MinimumDistance (InPut):
    min = len(InPut)
    temp=0
    #loop passing through the whole list calculating the minimum distance between each two equal nu.
    #and putting the value in temp variable
    for i in range (len(InPut)):
        for j in range (i+1,len(InPut)):
            if InPut[i]==InPut[j]:
                temp=(j-i)
                if temp < min :
                    min=temp
    print(min)

#Taking the input fromthe user
s= input()
#adding the input into a list
InPut=(s.split())
for i in range(len(InPut)):
  InPut[i]=int(InPut[i])

