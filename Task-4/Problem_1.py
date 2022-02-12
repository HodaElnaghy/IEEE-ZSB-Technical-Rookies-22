Input = list(map(int, input().split()))
min = len(Input) - 1
for i in range(len(Input)):
    for j in range(i+1,len(Input)):
        if Input[i]==Input[j]:
            if j-i < min:
              min=j-i
print(abs(min))