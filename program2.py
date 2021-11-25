#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random
score = 0

def addQuiz():
    for x in range(10):
        a = random.randint(0,99)
        b = random.randint(0,99)
        

questions = addQuiz()
