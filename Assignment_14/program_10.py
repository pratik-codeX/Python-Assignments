'''
10. Write a lambda function which accepts three numbers and returns largest number.
'''
    
###########################################################################
##   	Function Name  	:  ret_Large
##  	Description    	:  Check Prime
##  	Input          	:  int
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

ret_Large = lambda No1,No2,No3: No1 if No1 >= No2 and No1 >= No3 else No2 if (No2 >= No1 and No2 >= No3) else No3
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Flag = 0
    Value1 = 0
    Value2 = 0
    Value3 = 0

    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))
    Value3 = int(input("Enter Number :"))


    Flag = ret_Large(Value1,Value2,Value3)
    print(Flag)
    
if __name__ == "__main__":
    main()