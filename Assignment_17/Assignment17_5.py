###########################################################################
##   	Function Name  	:  ChkPrime
##  	Description    	:  Prime or not 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def ChkPrime(No):
    Flag = False
    for i in range(2,No//2):
        if No % i == 0:
            Flag = True
    
    return Flag
        
def main():
    Value = int(input("Enter Number :"))
    Ret = ChkPrime(Value)
    

    if(Ret == False):
        print("It is  Prime Number")
    else:
        print("It is Not Prime Number")
    
if __name__ == "__main__":
    main()