###########################################################################
##  Function Name  	:  Add
##  Description    	:  Addtion of number
##  Input          	:  
##	Output         	: 
##	Date           	:   6/7/2026
##  Author  		:   Pratik Raut
###########################################################################

def Add(No1,No2):
    return No1 + No2
      
###########################################################################
##  Function Name  	:  main
##  Description    	:  Client 
##  Input          	:  
##	Output         	: 
##	Date           	:   1/7/2026
##  Author  		:   Pratik Raut
###########################################################################

def main():
    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))

    Ret = Add(Value1,Value2)
    print(Ret)

if __name__ == "__main__":
    main()
