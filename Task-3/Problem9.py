def countingValleys(path):
    path=path.upper()
    for i in path:
        if i=='U' or i=='D':
            valleys=0
            lvl=0
            for i in path:
                if i=='U':
                    lvl+=1
                if i =='D':
                    lvl-=1
                if lvl ==0 and i =='U':
                    valleys+=1
            return valleys 
        else:
            print("Invalid input")
            return None
        
    

n = int (input("Enter the number of steps: "))
path= input("enter path:\n")
print (countingValleys(path))