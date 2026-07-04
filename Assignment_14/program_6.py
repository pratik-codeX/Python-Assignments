'''
6. Write a lambda function which accepts one number and returns True if number is odd
otherwise False
'''
    
###########################################################################
##   	Function Name  	:  ChkOdd
##  	Description    	:  Check Odd
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  4/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

ChkOdd = lambda No:(No % 2 != 0)
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Flag = False
    Value = 0

    Value = int(input("Enter Number :"))

    Flag = ChkOdd(Value) 
    print(Flag)
    
if __name__ == "__main__":
    main()