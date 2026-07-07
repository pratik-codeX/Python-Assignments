
##########################################################################
##   	Function Name  	:  Disaplay
##  	Description    	:  Star Printing
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def Dispaly(No):
    temp = No
    for i in range(No):
        temp = No
        print()
        while(temp != 0):
            print(f"{1 * " * "}",end="")
            temp = temp -1 
        
    print()

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

    Dispaly(Value)
   
if __name__ == "__main__":
    main()