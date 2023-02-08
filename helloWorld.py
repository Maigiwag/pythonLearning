#helloWorld.py

'''
Title: Hello world program
author: jason wang
date created: 2023-02-07
'''

#this is a print function

#print("Hello world!")


#variable types

x = 5
y = 7
#integer is a whole number

float1 = 8.5
float2 = 5.3
#floats number with decimals

string1 = "Hello World"
string2 = "8"
#string is a string of text

true  = True 
false = False
#booleans are true and false statements

'''
addtion = +
subtractoin = -
multiple = *
divide = /
'''

print(x + y)
print("x + y is equal to:", x+y)




while True: 
    userinput = input("please insert a number: ")
    try:
        userinput = int(userinput)
            
        print("your number plus 10 is:", userinput + 10)
        tryagain = input("Would you like to input another number y/n")
        if tryagain == "y":
            pass
        elif tryagain == "n":
            break
        else:
            print("Did not insert valid option, restarting program.")
            pass
    except:
        print("please input an integer")
        pass

print("loop is broken")
