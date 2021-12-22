def count_substring(string, sub_string):
    j=0
    flag=0
    counter=0
    for i in range(len(string)):
        if string[i] == sub_string[j]:

            flag=i-j-1
            if j+1<len(sub_string)-1:
                j+=1
            else:
                counter+=1
                i=i-j
                j=0

        else:
            if j!=0:
                i = flag

            j=0




    print( counter)

OriginalString=""

#Condition to make sure that 1<= string <= 200
while len(OriginalString) <1 or len(OriginalString)>200:
    OriginalString=input("Enter the original string: ")
    SubString=input("Enter the Sub string: ")

OriginalString.lower()
SubString.lower()
print(OriginalString)


count_substring(OriginalString.lower(), SubString.lower())