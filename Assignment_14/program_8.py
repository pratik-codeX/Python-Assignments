'''
8. Write a lambda function which accepts two numbers and returns addition.
'''
    
###########################################################################
##   	Function Name  	:  chkEven
##  	Description    	:  Check Even
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

ChkEven = lambda No1,No2: No1 + No2
    
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
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))

    Ret = ChkEven(Value1,Value2) 
    print(Ret)
    
if __name__ == "__main__":
    main()