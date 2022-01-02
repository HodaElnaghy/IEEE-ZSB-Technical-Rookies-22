#taking the input array in one line representing values of x1,v1 ,x2 and v2.
arr= list(map(int,input("Enter: ").strip().split()))[:4]
x1=arr[0]
v1=arr[1]
x2=arr[2]
v2=arr[3]
isPossible=False
# ensuring that the sign of the position difference and the sign of the velocity difference are opposite
if (x1-x2)*(v1-v2) <0 :
    if(x2-x1)%(v1-v2)==0:  #if the 2 kangaroos met the (x2-x1)/(v1-v2) would be a real integer no.
        isPossible=True
#printing results
if isPossible:
    print('Yes')
else:
    print('No')