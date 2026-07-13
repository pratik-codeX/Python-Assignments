'''
4. Write a program that calculates
1^5+2^5+3^5+…..+N^5
for multiple values of N simultaneously using Pool.
Input
[1000000,
2000000,
3000000,
4000000]
Measure total execution time.
'''
import multiprocessing
import os 
import time

def Multi(No):
    Multi = 1
    Sum = 0
    for i in range(1,No+1):
        for j in range(5):
            Multi = i * Multi

    return Multi

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    List = [1000,50,20]

    start_time = time.perf_counter()
    tobj = multiprocessing.Pool()

    Result = tobj.map(Multi,List)
    
    print(Result)

    end_time = time.perf_counter()   

    print(f"Time for executetion is :{end_time - start_time}") 
if __name__ == "__main__":
    main()