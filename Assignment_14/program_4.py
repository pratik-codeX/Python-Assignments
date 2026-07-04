'''
4. Write a lambda function which accepts two numbers and returns minimum number.
'''
###########################################################################
##   	Function Name  	:  DisplayBinary
##  	Description    	:  Check Prime
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

Minimum = lambda No1,No2 : No1 < No2

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
    Value1 = int(input("Enter first Number :"))
    Value2 = int(input("Enter second Number"))

    Flag = Minimum(Value1,Value2)
    
    if(Flag == True):
        print(Value1,"is Minimum")
    else:
        print(Value2,"is Minimum")

if __name__ == "__main__":
    main()