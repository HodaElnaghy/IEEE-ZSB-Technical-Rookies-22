# creating an array (count) its indices represents the id no. from 0 to 5
# and the value of each index represent frequency of each type
# the function the index of the most frequently sighted bird
def migratoryBirds(id):
    count = [0]*6
    for i in id :
        count[i]+=1
    return count.index(max(count))

n = int (input("Enter the no. of birds sighted: "))
id = list(map(int,input("Enter the types of birds sighted: ").strip().split()))[:n] 
print (migratoryBirds(id))