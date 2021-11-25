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
    if a>=b and a>=c and a>=d :
        largest = a
        if b>c and b>d and c>d :
            middle2 = b
            middle = c
            smallest = d
        elif b<c and b>d and c>d :
            middle2 = c
            middle = b
            smallest = d
        elif b>c and b>d and c<d :
            middle2 = b
            middle = d
            smallest =c
        elif b>c and b<d and c<d :
            middle2 = d
            middle = b
            smallest = c
        else :
            middle2 = d
            middle = c
            smallest = b
    if b>=a and b>=c and b>=d :
        largest = b
        if a>c and a>d and c>d :
            middle2 = a
            middle = c
            smallest = d
        elif a<c and a>d and c>d :
            middle2 = c
            middle = a
            middle = d
        elif a>c and a>d and c<d :
            middle2 = a
            middle = d
            smallest = c
        elif a>c and a<d and c<d :
            middle2 = a
            middle = d
            smallest = c
        else :
            middle2 = d
            middle = b
            smallest = a
    if c>=a and c>=b and c>=d :
        largest = c
        if a>b and a>d and b>d :
            middle2= a
            middle = b
            smallest = d
        elif a<b and a>d and b>d :
            middle2 =  b
            middle = a
            smallest = d
        elif a>b and a>d and b<d :
            middle2 = a
            middle = d
            smallest = b
        elif a>b and a<d and b<d :
            middle2 = d
            middle = a
            smallest = b
        else :
            middle2 = d
            middle = b
            smallest = a
    if d>=a and d>=b and d>=c :
        largest = d
        if a>b and a>c and b>c :
            middle2 = a
            middle = b
            smallest = c 
        elif a<b and a>c and b>c :
            middle2 = b
            middle = a
            smallest = c 
        elif a>b and a>c and b<c :
            middle2 = a
            middle = c
            smallest = b
        elif a>b and a<c and b<c :
            middle2 = c
            middle = a
            smallest = b
        else:
            middle2 = c
            middle = b
            smallest = a
    return largest, middle2, middle, smallest
def display(number):
    print("The numbers from highest to lowest are:" ,largest,middle2,middle,smallest)

#step1
number = enterNumber()
#step2
ifelse = evaluate()
#step3
display(number)