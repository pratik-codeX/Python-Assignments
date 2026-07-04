'''
7. Write a lambda function which accepts one number and returns True if divisible by 5
'''
    
###########################################################################
##   	Function Name  	:  DisplayBinary
##  	Description    	:  Check Prime
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

CheckDivisible = lambda No : (No % 5 == 0)
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Flag = False
    Value = 0
    Value = int(input("Enter Number :"))
    Flag = CheckDivisible(Value)
    print(Flag)

if __name__ == "__main__":
    main()