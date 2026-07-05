'''
1. Write a lambda function using map() which accepts a list of number and return a list of squares of
each number. 
'''
Square = lambda No : No*No

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Ret = list()
    Arr = [10,20,30,40,51]

    Ret = list(map(Square,Arr))

    print(Ret)

if __name__ == "__main__":
    main()