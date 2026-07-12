'''
2. Write a program that calculates factorials of multiple numbers
simultaneously using Pool.map().
Input
[10,15,20,25]
Display
•
•
•
Process ID
Input Number
Factorial
'''
import multiprocessing

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
        
    return Fact

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   11/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Lst = []
    No = 0
    Size = int(input("Enter the size of list :"))

    for i in range(Size):
        No = int(input("Enter number :"))
        Lst.append(No)

    print(Lst)

    p1 = multiprocessing.Pool()

    Ret = p1.map(Factorial,Lst)

    print(Ret)

if __name__ == "__main__":
    main()
    print("Exit from main")