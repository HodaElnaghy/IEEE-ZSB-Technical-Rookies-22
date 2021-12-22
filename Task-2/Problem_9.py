#Function prints the diffrence between two diagonals
def diffrence(matrix):
    Diagonal1 = 0
    Diagonal2 = 0
    Diff = 0
    for i in range(N):
        Diagonal1 += matrix[i][i]
        Diagonal2 += matrix[N - i - 1][i]
    Diff = Diagonal1 - Diagonal2
    print(Diff)


condition = True
arr=[]
#condition that gives error if the use enters input out of range [-100,100]
while condition:
    matrix=[]
    N=int(input(" Enter the matrix order: "))

    #taking input og matrix from user
    for i in range (N):
        s = input("Enter matrix numbers: ")
        # adding the input into a list
        arr = (s.split())
        matrix.append([])
        for j in range(N):
            matrix[i].append(int(arr[j]))
            if matrix[i][j] >100 or matrix[i][j]<-100:
                condition=false
    condition=False

diffrence(matrix)



