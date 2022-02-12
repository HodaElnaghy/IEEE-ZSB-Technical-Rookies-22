def findDigits(n):
    temp = n
    counter = 0
    while n != 0:
        digit = n % 10
        n //= 10
        if digit != 0 and temp % digit == 0:
            counter += 1
    return counter


if __name__ == '__main__':
    t = int(input("Enter the no. of test cases: "))
    for i in range(t):
        n = int(input())
        print(findDigits(n))

