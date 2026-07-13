'''
Write a program that calculates factorials of multiple numbers
simultaneously using multiprocessing.Pool.
'''
import multiprocessing
import os

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
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    No = [20]

    tobj = multiprocessing.Pool()

    result = tobj.map(Factorial,No)

    print("Pid is :",os.getpid())
    print(result)

if __name__ == "__main__":
    main()