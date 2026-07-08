'''
4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''

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