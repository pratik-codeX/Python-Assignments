###########################################################################
##   	Function Name  	:  CountDigit
##  	Description    	:  Digit Counting in number
##  	Input          	:  int
##	    Output         	:  int
##	    Date           	:  4/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

def CountDigit(No):
    Digit = 0
    Count = 0
    while(No != 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10
    
    return Count

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))

    Ret = CountDigit(Value)
    print(Ret)
    
if __name__ == "__main__":
    main()