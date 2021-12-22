# Returns reverse of a string
def isPalindrome(y):
    return y == y[::-1]


# take an input from the user
s = input("Enter a word:")
ans = isPalindrome(s)

#Checking if it is palindrome or not
if ans:
    print("Yes")
else:
    print("No")