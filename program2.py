#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random
score = 0
quesNum = 1


for x in range(10):
    a = random.randint(0,99)
    b = random.randint(0,99)
    print("Question",quesNum,":\nWhat is ",a,"+",b,"?" )
    ans = int(input("="))
    rightAns = a + b
    if ans == rightAns:
        print("Correct!")
        score = score + 1
    else:
        print (f"Wrong! The correct Answer is {rightAns}.")
quesNum = quesNum+1
        
