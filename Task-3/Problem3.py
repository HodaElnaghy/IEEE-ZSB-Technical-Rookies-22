import string
import random
#Creating a list of all lowercase letters
lowChar = string.ascii_lowercase
lowChar = list(lowChar)
#Creating a list of all uppercase letters
uppChar = string.ascii_uppercase
uppChar = list(uppChar)
#Creating a list of all digits from 0 to 9
digits = string.digits
digits = list(digits)
#Creating a list of all special characters
symbols = ['@','#' ,'$', '%', '&']
#Combination
combinedList = lowChar+uppChar+digits+symbols
# randomly select at least one character from each type 
rand_digit = random.choice(digits)
rand_upper = random.choice(uppChar)
rand_lower = random.choice(lowChar)
rand_symbol = random.choice(symbols)
#we need to make sure that password contains at least 1 of each character type
passWord= rand_digit + rand_upper + rand_lower + rand_symbol
#chosing random values from Combination List for the rest of the password
for i in range (6):
    passWord += random.choice(combinedList)
#setting the password into list and shufffle it 
Pass= list(passWord)
random.shuffle(Pass)
#setting the list elements into the password
passWord=""
for ele in Pass:
    passWord+=ele
print(passWord)