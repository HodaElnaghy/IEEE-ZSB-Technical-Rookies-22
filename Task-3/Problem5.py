n = int (input("Enter the no. of games: "))
scores = list(map(int,input("Enter the score of each game: ").strip().split()))[:n]
max=scores[0]
min=scores[0]
maxCounter=0
minCounter=0
for i in scores:
    if i>max:
        max=i
        maxCounter+=1
    if i<min:
        min=i
        minCounter+=1
print(f'{maxCounter} , {minCounter}')
