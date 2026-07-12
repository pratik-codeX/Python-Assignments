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
        for j in range(2,i):
            print(j,"Dividing to ",i)
            if i % j == 0:
                print(i)
            
            
                
                

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    No = 16

    Ret = CountPrime(No)

    
if __name__ == "__main__":
    main()