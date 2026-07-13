'''
Design a Python application that creates two threads.
•Thread 1 should compute the sum of elements from a list.
•Thread 2 should compute the product of elements from the same list.
•Return the results to the main thread and display them.
'''

import multiprocessing

List = [10,20,30]
Sum = 0
Multi = 0

def CountOdd(No):
    Sum = 0
    Count = 0
    for i in range(No):
        if i % 2 != 0:
            Count = Count +1
        
    return Count

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   8/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [100,200,300,400]
    
    tobj = multiprocessing.Pool()

    Result = tobj.map(CountOdd,Arr)
   
    print(Result)
if __name__ == "__main__":
    main()