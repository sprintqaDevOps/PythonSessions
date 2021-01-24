#Write a program that allows the user to enter any number of test scores. 
# The user indicates they are done by entering in a negative number. 
# Print how many of the scores are A’s (90 or above). 
# Also print out the average. 

userInputs = []
numGreater90 = []
score = 0

while score >= 0:
    score = int(input("Put a number, to exit enter a negative number: "))
    if score >= 90:
        userInputs.append(score)
        numGreater90.append(score)
    elif score >= 0:
        userInputs.append(score)
    else:
        print("number is out of range")
print(userInputs)
print(numGreater90)
print("Bigger than 90: ", len(numGreater90))
print("Avarege: ", sum(userInputs)/len(userInputs))
# sum of all items/number of all items

# total=0
# avg=total/len(userInputs)
# for i in userInputs:
#     total+=i
# print(avg)
