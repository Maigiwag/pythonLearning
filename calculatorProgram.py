#calculatorProgram.py

'''
Tite: Calculator Program
Author: Jason Wang
Date-Created: 2023-02-08
'''

#---INPUT---#

def getNumber():
    '''
    This function will retrieve a number from the user
    '''
    userinput = input("give number: ")
    userinput = isNumeric(userinput)
    if userinput == False:
        return getNumber()
    else:
        return userinput


def opertationChoice():
    '''
    User picks which opertation to use
    '''
    print('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    ''')
    choice = input("> ")
    choice = isNumeric(choice)
    if choice > 0 and choice < 5:
        return choice
    else:
        print("Sorry, please choose a valid number")
        return opertationChoice()

        
#---PROCESSING---#

def isNumeric(userinput):
    '''
    This function will check if user input is valid
    '''

    try: 
        userinput = int(userinput)
        return userinput
    except:
        print("Please pick a valid number")
        return False


def addition(numb1, numb2):
    '''
    This function will add two variables
    '''
    answer = numb1 + numb2
    return answer


#---OUTPUT---#


def displayAnswer(answer):
    '''
    Function will display the answer to the user
    ''' 

    print("The solution to your calculation is : ", answer)    


##---MAIN PROGRAM CODE---##

while True:
   
    input1 = getNumber()
    input2 = getNumber()
    choice = opertationChoice()
    if choice == 1:
        answer = addition(input1, input2)
    displayAnswer(answer)
    

