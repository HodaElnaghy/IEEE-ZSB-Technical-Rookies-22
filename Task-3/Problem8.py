# sockMerchant function creates a list of the odd pairs 
# then calculate the number of pirs through ((no.of all socks-no. of odd socks)/2)
def sockMerchant(arr):
    counter=[]
    for i in arr:
        if i not in counter:
            counter.append(i)
        else:
            counter.remove(i)
    pairs = int((len(arr)-len(counter))/2)
    return pairs

n = int (input("Enter the number of socks in the pile: "))
arr = list(map(int,input("Enter the colors of each sock: ").strip().split()))[:n]
print (sockMerchant(arr))
