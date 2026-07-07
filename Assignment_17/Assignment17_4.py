###########################################################################
##   	Function Name  	:  FactAddition
##  	Description    	:  Factorial numbers Addition 
##  	Input          	:  12
##      Output         	:  16 (1+2+3+4+6)
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

def FactAddtion(No):
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = i + Sum
    
    return Sum


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))

    Ret = FactAddtion(Value)

    print(Ret)

if __name__ == "__main__":
    main()