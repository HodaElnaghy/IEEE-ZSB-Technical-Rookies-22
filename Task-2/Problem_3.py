import random

#comparing method that compares every digit with it's corresponding
def Comp(rand,InPut):
    Hit=0
    Miss=0
    Temp1=[]
    Temp2=[]
    for i in range (3):
        if rand[i]==InPut[i]:
            Hit+=1
        else:   #excluding the hitted numbers from the list and comparing again to see if there is any missed number
            Temp1.append(rand[i])
            Temp2.append(InPut[i])
    for i in range(len(Temp1)):
        for j in range(len(Temp1)):
            if Temp1[i] == Temp2[j]:
                Miss+=1


    return (Hit,Miss)


Hit=0
Miss=0
#initiating a 3 digits random number
rand = int(random.random() * 1000)
#putting the random number in a list to be able to compare
u1 = rand % 10
t1 = int((rand / 10) % 10)
h1 = int(rand / 100) % 10
randlist = [u1, t1, h1]

#loop to keep taking the input if doens'nt totally match the random number
while Hit != 3:
    #taking the input number and putting it into a list
    InPut= int(input("Enter a 3 digits number:"))
    u= InPut % 10
    t=int((InPut/10)%10)
    h=int(InPut/100)%10
    InPutlist=[u,t,h]

    #passing the random list and input list to the comparing function
    Hit,Miss= Comp(randlist,InPutlist)
    #printing the ratio
    print(Hit,'Hit',Miss,'Miss')
#after guessing the correct number finally ending the program
print('you have guessed it right')



