import math
seqOfLetters = input("Enter the sequence of letters: ")
n = int(input("Enter n : "))
str= seqOfLetters* math.ceil(n/len(seqOfLetters))
counter= 0
for i in range(10):
    if str[i]=='r' or str[i]=='R':
        counter+=1
print(counter)