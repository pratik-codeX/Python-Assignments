###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def ChkNum(No):
    if(No == 0):
        print("Zero")
    elif(No > 0):
        print("Positive Number")
    else:
        print("Negative Number")
    
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))

    ChkNum(Value)
    
    
if __name__ == "__main__":
    main()