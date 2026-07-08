'''
3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
'''

from functools import reduce

ChkGreater = lambda No : (No >= 70 and No <= 90)

Increment = lambda No : No + 10

Product = lambda No1,No2 : No1 * No2

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FRet = list(filter(ChkGreater,List))

    print(f"List after Filter :{FRet}")

    MRet = list(map(Increment,FRet))
    print(f"List after Map :{MRet}")

    RRet = reduce(Product,MRet)
    print(f"List after Reduce :{RRet}")

if __name__ == "__main__":
    main()