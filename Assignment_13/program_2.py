'''
2. Write a program which accepts radius of circle and prints area of circle.
'''
###########################################################################
##   	Function Name  	:  Area
##  	Description    	:  Area of Circle
##  	Input          	:  int,int
##	    Output         	:  int
##	    Date           	:  1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


def Area(Radi,Pi = 3.14):
    Area = 0
    Area = Pi * Radi * Radi
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
    Value2 = 3.14
    Value1 = int(input("Enter the Number :"))

    Ret = Area(Value1,Value2)
   
    print("Area is :",Ret)
   
if __name__ == "__main__":
    main()