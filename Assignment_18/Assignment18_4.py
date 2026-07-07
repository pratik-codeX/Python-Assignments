
##########################################################################
##   	Function Name  	:  Disaplay
##  	Description    	:  Star Printing
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   6/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def FindFrequency(Arr,No):
    Count = 0
    for i in Arr:
        if i == No:
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
    lst = []
    result = 0
    Size = int(input("Enter Number of elements : "))
    print("*"*50)
    print("Input Elements :")

    for i in range(Size):
        result = int(input(f"Element Number {i} :"))
        lst.append(result)

    Value = int(input("Enter Element to Search :"))
    
    Ret = FindFrequency(lst,Value)
    print(Ret)

   
if __name__ == "__main__":
    main()