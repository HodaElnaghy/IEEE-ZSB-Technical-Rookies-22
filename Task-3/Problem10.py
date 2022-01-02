def pageCount(n, p):
    totalTurns=int(n/2)
    frontTurns=int(p/2)
    backTurns=int(totalTurns-frontTurns)
    return(min(frontTurns,backTurns))

n=int(input('Enter no. of pages: '))
p=int(input('Enter the page number to turn to: '))
print(pageCount(n,p))
