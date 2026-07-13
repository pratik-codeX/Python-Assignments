'''
3. For every number in the given list, count how many prime numbers
exist between 1 and N using multiprocessing Pool.
Example
10000
20000
30000
40000
Display total prime count for each number.
'''
import multiprocessing

def CountPrime(No):
    Count = 0
    for i in range(2,No+1):
        Flag = True
        for j in range(2,i+1//2):
            if i % j == 0:
                Flag = False

        if Flag == True:
            Count = Count + 1

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
    No = [10000,20000,30000,400000]

    tobj = multiprocessing.Pool()

    Result = tobj.map(CountPrime,No)
    
    print(Result)
    
if __name__ == "__main__":
    main()