
###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   4/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def Divisiblebyfive(No):
    if(No % 5 == 0):
        return True
    else:
        return False
    
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

    Ret = Divisiblebyfive(Value)
    print(Ret)
    
if __name__ == "__main__":
    main()