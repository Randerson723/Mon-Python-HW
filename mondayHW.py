#create a calculator using functions that asks for two numbers
#performs a calculation that the user inputs


def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1+num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

value1 = int(input("num1"))
value2 = int(input("num2"))

input("Operation selectors 1-addition, 2-Subtraction, 3-multiplication, 4-Division")
operation = int(input("choose 1, 2, 3, 4: "))

if operation == 1:
    print(value1, "+", value2, "=", addition(value1,value2))

    if operation == 2:
        print(value1, "-", value2, "=", subtraction(value1, value2))

    if operation == 3:
        print(value1, "*", value2, "=", multiplication(value1, value2))

    if operation == 4:
        print(value1, "/", value2, "=", division(value1, value2))

    else:
        print("Enter correct operation")

#Create a pyramid of x's for n, number of levels
# I found this code but wasn't able to get it to work 
def pyramid(n):
    mylist = []
    for i in range(0,n):
        for j in range(0,k):
            print(end="")
            k = k -1
            for j in range(0, i+1):
               print("*", end="") 

            print("\r")
        n=(5)

        pyramid(n)