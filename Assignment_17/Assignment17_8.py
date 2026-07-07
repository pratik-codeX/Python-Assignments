###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def Display(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            if i == j or i >= j:
                print(j,"\t",end="")
            
        print()
                
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