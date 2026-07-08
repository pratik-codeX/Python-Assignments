import threading

def Disaplay():
    for i in range(1,50+1):
        print(i)

    print("Thread 1 execution Stops")


def DisaplayReverse():
    for i in range(50,1,-1):
        print(i)

    print("Thread 2 execution Stops")


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

    Disaplay()
    DisaplayReverse()
   
if __name__ == "__main__":
    main()