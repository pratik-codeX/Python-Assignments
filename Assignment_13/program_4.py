'''
4. Write a program which accepts one number and prints binary equivalent.
'''
###########################################################################
##   	Function Name  	:  DisplayBinary
##  	Description    	:  Check Prime
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

def DisplayBinary(No):
    Binary = 0
    Digit = 0
    while(No != 0):
        Binary = No % 2
        print(Binary)
        No = No // 2

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = 0
    Value = int(input("Enter Number :"))
    DisplayBinary(Value)
    
if __name__ == "__main__":
    main()