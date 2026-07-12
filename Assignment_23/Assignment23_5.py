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

def Multi(No):
    Multi = 1
    Sum = 1
    for i in range(1,No+1):
        for j in range(1,5+1):
            Multi = j * Multi 

        print(Multi)
                

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    No = 5

    tobj = multiprocessing.Pool()

    Multi(No)
    #Result = tobj.map(Multi,No)
  

if __name__ == "__main__":
    main()