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

    tobj1 = threading.Thread(target=Disaplay)
    tobj2 = threading.Thread(target=DisaplayReverse)

    tobj1.start()
    tobj1.join()


    tobj2.start()
    tobj2.join()
   
if __name__ == "__main__":
    main()