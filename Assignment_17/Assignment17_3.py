###########################################################################
##  Function Name  	:  Factorial
##  Description    	:  Factorial
##  Input          	:  5
##	Output         	:  120
##	Date           	:   6/7/2026
##  Author  		:   Pratik Raut
###########################################################################

#!5 = 5*4*3*2*1

def Factorial(No):
    Sum = 1
    for i in range(1,No+1):
       
        Sum = Sum * i

    return Sum
      
###########################################################################
##  Function Name  	:  main
##  Description    	:  Client 
##  Input          	:  
##	Output         	: 
##	Date           	:   1/7/2026
##  Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))
    Ret = Factorial(Value)

    print(Ret)

if __name__ == "__main__":
    main()
