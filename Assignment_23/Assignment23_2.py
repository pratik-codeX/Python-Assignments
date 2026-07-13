'''
Write a Python program using multiprocessing.Pool to calculate the
sum of all odd numbers from 1 to N.
'''
import multiprocessing
import os

def SumOdd(No):
    Sum = 0
    for i in range(No+1):
        if i % 2 != 0:
            Sum = i + Sum
        
    return Sum

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   11/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Lst = [1000000]

    p1 = multiprocessing.Pool()

    Ret = p1.map(SumOdd,Lst)

    print("Process id is :",os.getpid())
    print(Ret)

if __name__ == "__main__":
    main()
    