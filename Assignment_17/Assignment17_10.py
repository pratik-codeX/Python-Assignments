###########################################################################
##   	Function Name  	:  DigitSum
##  	Description    	:  Digit Addition 
##  	Input          	:  int
##	    Output         	:  int
##	    Date           	:  7/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

def DigitSum(No):
    Digit = 0
    DigitSummation = 0
    while(No != 0):
        Digit = No % 10
        DigitSummation = Digit + DigitSummation
        No = No // 10
    
    return DigitSummation

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   7/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))

    Ret = DigitSum(Value)
    print(Ret)
    
if __name__ == "__main__":
    main()