'''
4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
all elements.
'''

from functools import reduce

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [11,21,51,101]
    
    Ret = reduce(lambda x,y: x + y,Arr)
    print(Ret)

if __name__ == "__main__":
    main()