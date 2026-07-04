'''
3. Write a lambda function which accepts two numbers and returns maximum number.
Input: 6
Output: Perfect Number
'''
###########################################################################
##      Function Name  	:  ChkMaximum
##  	Description    	:  Maximum numbers
##  	Input          	:  int,int
##      Output         	:  int
##	    Date           	:  1/7/2026
##  	Author  		:  Pratik Raut
###########################################################################

Max = Maximum = lambda No1 , No2 : No1 > No2
      
###########################################################################
##  Function Name  	:  main
##  Description    	:  Client 
##  Input          	:  
##	Output         	: 
##	Date           	:   1/7/2026
##  Author  		:   Pratik Raut
###########################################################################

def main():
    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))
    Flag = False
    
    Flag = Maximum(Value1,Value2)

    if(Flag == True):
        print(Value1,"is Maximum")
    else:
        print(Value2,"is Maximum")

if __name__ == "__main__":
    main()
