###########################################################################
##   	Function Name  	:  Display
##  	Description    	:  
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def Display(No):
    for i in range(No,0,-1):
        print(f"{i * " * "}")
        
    
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

    Display(Value)
    
    
if __name__ == "__main__":
    main()