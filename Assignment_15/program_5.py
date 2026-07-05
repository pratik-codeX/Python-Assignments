''' 
5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
element.
'''
from functools import reduce

FindMax = lambda No1,No2 : No1 if(No1> No2) else No2
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [100,200,30,-1]

    Ret = int(reduce(FindMax,Arr))
    print(Ret)
    
if __name__ == "__main__":
    main()