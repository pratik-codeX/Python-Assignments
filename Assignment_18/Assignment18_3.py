
##########################################################################
##   	Function Name  	:  Disaplay
##  	Description    	:  Star Printing
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def MinimunInList(Arr):
    Min = Arr[0]
    for i in Arr:
        if i < Min:
            Min = i
 
    return Min

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
    print("*"*50)
    print("Input Elements :")

    for i in range(Size):
        
        result = int(input(f"Element Number {i} :"))
        lst.append(result)

    Ret = MinimunInList(lst)
    print(Ret)

   
if __name__ == "__main__":
    main()