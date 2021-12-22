#Taking input from the user
s= input()

#Splitting the input and putting it into list
InPut=(s.split())

#Converting the input from string to integer
for i in range(len(InPut)):
  InPut[i]=int(InPut[i])

#Removing duplicates
OutPut = list(set(InPut))
#Printing the removed duplicates list
OutPut.sort()
print(OutPut)

