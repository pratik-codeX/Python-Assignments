'''
1. Write a program which accepts length and width of rectangle and prints area.
'''
###########################################################################
##   	Function Name  	:  Area
##  	Description    	:  Area of Rectangle
##  	Input          	:  int,int
##	    Output         	:  int
##	    Date           	:  1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


def Area(No1,No2):
    Area = 0
    Area = No1 * No2
    return Area

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
    Value1 = int(input("Enter the Number :"))
    Value2 = int(input("Enter the Number :"))

    Ret = Area(Value1,Value2)
   
    print("Area is :",Ret)
   
if __name__ == "__main__":
    main()