
##########################################################################
##   	Function Name  	:  Disaplay
##  	Description    	:  Star Printing
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def ListAdditon(Arr):
    Sum = 0
    for i in Arr:
        Sum = Sum + i
        
    return Sum

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    lst = []
    result = 0
    Size = int(input("Enter Number of elements : "))
    print("*"*15)
    print("Input Elements :")

    for i in range(Size):
        
        result = int(input(f"Element Number {i} :"))
        lst.append(result)

    Ret = ListAdditon(lst)
    print(Ret)

   
if __name__ == "__main__":
    main()