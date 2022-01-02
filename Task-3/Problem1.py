n= int(input("enter the no. of bottels: ")) 
volume=[]
capacity=[]
totalVolume=0
#setting the remaining volumes and capacities into lists
for i in range (n):
    volume.append(int(input(f'enter the remainning volume for bottele no.{i+1}: ')))
    capacity.append(int(input(f'enter botttel no.{i+1} capacity: ')))

# finding the 2 bottels with the largest capacities 
sumMaxBottels= max(capacity)
capacity.remove(max(capacity))
sumMaxBottels+=max(capacity)
# finding the total remaining volume
for i in volume:
    totalVolume+=i
# checking if you can pour all the water into 2 bottles
isEnough=True
if sumMaxBottels < totalVolume :
    isEnough=False
# printing results
if isEnough:
    print("Yes")
else:
    print("No")
