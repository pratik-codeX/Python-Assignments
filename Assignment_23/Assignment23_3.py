'''
Write a program that counts how many even numbers exist
between 1 and N using Pool.map().
'''
import multiprocessing

def CountEven(No):
    Sum = 0
    Count = 0
    for i in range(No):
        if i % 2 == 0:
            Count = Count +1
        
    return Count
            
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [1000000, 2000000, 3000000, 4000000]
    
    tobj = multiprocessing.Pool()

    Result = tobj.map(CountEven,Arr)
    
    print(Result)

    
if __name__ == "__main__":
    main()