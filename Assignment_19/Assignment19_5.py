from functools import reduce

def is_Prime(No):
    Flag = True
    for i in range(2,No+1//2):
        if No % i == 0:
            Flag = False
            break
        
    return Flag

Multi = lambda x : x * 2

Max = lambda x , y : x if x > y else y

def Maximum(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():

    List = list()

    Size = int(input("Enter No of elements : "))

    for i in range(Size):
        No = int(input(f"Enter Number :{i} : "))
        List.append(No)

    FRet = list(filter(is_Prime,List))

    MRet = list(map(Multi,FRet))

    RRet = reduce(Maximum,MRet)

    print(RRet)
   
if __name__ == "__main__":
    main()