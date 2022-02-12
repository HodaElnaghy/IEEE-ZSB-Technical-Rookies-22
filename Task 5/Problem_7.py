def acmTeam(topic):
    maxSub=0
    teamCount=0
    result=[]
    for i in range(n):
        for j in range(i+1,n):
            if i==j:
                continue
            else:
                sum=bin(int(topic[i], 2) | int(topic[j], 2))[2:].count('1')
                if sum>maxSub:
                    maxSub=sum
                    teamCount=1
                elif sum==maxSub:
                    teamCount+=1
    result.append(maxSub)
    result.append(teamCount)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    topic= [input() for _ in range(n)]
    result = acmTeam(topic)
    print(result)