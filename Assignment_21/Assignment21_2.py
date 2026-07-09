'''
: Design a Python application that creates two threads.
•Thread 1 should calculate and display the maximum element from an list.
•Thread 2 should calculate and display the minimum element from the same list.
•The list should be accepted from the user.
'''
import threading

def MaxElement(Arr):
    Max = Arr[0]

    for i in Arr:
        if Max < i :
            Max = i
    
    print(Max)

def MinElement(Arr):
    Min = Arr[0]

    for i in Arr:
        if Min > i :
            Min = i
    
    print(Min)


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Lst = [10,2,30,40,5]
    #Value = int(input("Enter Number :"))

    Thread1 = threading.Thread(target=MaxElement,args=(Lst,))
    Thread2 = threading.Thread(target=MinElement,args=(Lst,))
    
    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":
    main()
    print("Exit from main")