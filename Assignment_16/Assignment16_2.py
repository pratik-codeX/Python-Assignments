
###########################################################################
##   	Function Name  	:  ChkNum
##  	Description    	:  Even Odd 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))
    ChkNum(Value)
   
if __name__ == "__main__":
    main()