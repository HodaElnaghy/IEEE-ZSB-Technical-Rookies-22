#initiating array for number of days and time needed to read the book
arr_n_t=[]
time=0
days=0
condition1=True
while condition1:
    #putting the input in an array and converting it to integers
    s = input("Enter days and time: ")
    arr_input1 = (s.split())
    for i in range (2):
        arr_n_t.append(int(arr_input1[i]))

    #time needed to finish the book and nu of work days
    time = arr_n_t[1]
    days= arr_n_t[0]
    if (time>0 and time<10000000):
        if(days >0 and days<100):
            break

#for every day there is time for work, so putting the input in anothe array

while condition1:
    x = 0
    arr_workTime=[]
    s1 = input("Enter work time: ")
    arr1 = (s1.split())
    for i in range(days):
        arr_workTime.append(int(arr1[i]))
        if(arr_workTime[i]<=86400 and arr_workTime[i]>=0):
            x+=1
    if (x==days):
        break


n=0

#subtracting the time needed for work and finding if there still time to read
#Subtracting the needed for reading from the time left in the day after finishing work
for i in range (days):
    Seconds=86400
    Seconds-= arr_workTime[i]

    if (Seconds>0):
        time-=Seconds

    if (time<=0):
        print(i+1)
        break




