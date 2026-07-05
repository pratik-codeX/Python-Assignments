'''
9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
elements.
'''
from functools import reduce

Product = lambda No1 , No2 : No1 * No2
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [1,2,3]

    Ret = reduce(Product,Arr)
    print(Ret)
    
if __name__ == "__main__":
    main()