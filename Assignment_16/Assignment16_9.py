###########################################################################
##   	Function Name  	:  Display
##  	Description    	:  Even Numbers  
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def Display(No):
    for i in range(1,No+1):
        print(f"{i*2}\t",end="")
    
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
    Display(Value)
    
if __name__ == "__main__":
    main()