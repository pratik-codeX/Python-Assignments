##########################################################################
##   	Function Name  	:  LenStr
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def LenStr(Arr):
    Count = 0
    for i in Arr:
        Count = Count + 1

    return Count

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


def main():
    Str = input("Enter Text :")

    Ret = LenStr(Str)

    print(Ret)
    
if __name__ == "__main__":
    main()