'''
1. Write a lambda function which accepts one number and returns square of that number.
'''
###########################################################################
##   	Function Name  	:  SquareX
##  	Description    	:  Square of Number 
##  	Input          	:  int
##	    Output         	:  int
##	    Date           	:  2/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

Square = SquareX = lambda No : (No*No)


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Ret = 0
    No = int(input("Enter Number :"))

    Ret = SquareX(No)

    print(Ret)

if __name__ == "__main__":
    main()