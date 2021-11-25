#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.
def enterNumber():
    global a, b, c, d
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))
    d = int(input("Enter Fourth Number: "))
    return a, b, c, d

def evaluate():
    global largest,middle2,middle,smallest
    largest,middle2,middle,smallest =  0,0,0,0
    if a>=b and a>=c and a>=d:
        largest = a
        if b>c and b>d and c>d:
            middle2 = b
            middle = c
            smallest = d
        elif b<c and b>d and c>d:
            middle2 = c
            middle = b
            smallest = d
        elif b>c and b>d and c<d:
            middle2 = b
            middle = d
            smallest =c
        elif b>c and b<d and c<d:
            middle2 = d
            middle = b
            smallest = c
        else:
            middle2 = d
            middle = c
            smallest = b
    return largest, middle2, middle, smallest
#step1
number = enterNumber()
#step2
ifelse = evaluate()