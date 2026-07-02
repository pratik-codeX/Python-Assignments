'''
3. Write a program which accepts one number and checks whether it is perfect number or
not.
Input: 6
Output: Perfect Number
'''
###########################################################################
##   	Function Name  	:  ChkPrime
##  	Description    	:  Check Prime
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################


def ChkPerfect(No):
    Flag = False
    FactSum = 0
    for i in range(1,No+1//2):
        if(No % i == 0):
            FactSum = i + FactSum
    
    if(FactSum == No):
        Flag = True
        return Flag

    return Flag
        
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
    Flag = False
    Ret = False
    Value = int(input("Enter Number :"))
    Ret = ChkPerfect(Value)
    
    if(Ret == True):
        print("This is Perfect Number")
    else:
        print("This is Not Perfect Number")

if __name__ == "__main__":
    main()