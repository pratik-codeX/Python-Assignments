from functools import reduce

isEven = lambda No : (No % 2 == 0)

CalculateSquare = lambda No : No * No

Summation = lambda No1,No2 : No1 + No2


##########################################################################
##   	Function Name  	:  Disaplay
##  	Description    	:  Star Printing
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FRet = list(filter(isEven,List))

    MRet = list(map(CalculateSquare,FRet))
    print(MRet)

    RRet = reduce(Summation,MRet)

    print(RRet)
    
if __name__ == "__main__":
    main()