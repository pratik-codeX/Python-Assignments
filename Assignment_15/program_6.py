'''
6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum
element.
'''

from functools import reduce

MinMum = lambda No1,No2 : No1 if(No1<No2) else No2
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [10,-1,30,-7]

    Ret = reduce(MinMum,Arr)

    print(Ret)
    
if __name__ == "__main__":
    main()