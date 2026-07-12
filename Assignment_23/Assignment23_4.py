'''
Design a Python application that creates two threads.
•Thread 1 should compute the sum of elements from a list.
•Thread 2 should compute the product of elements from the same list.
•Return the results to the main thread and display them.
'''

import threading

List = [10,20,30]
Sum = 0
Multi = 0

def Sum():
    global List
    global Sum
    Sum = 0
    for i in List:
        Sum = Sum + i

def  Multi():
    global List
    global Multi
    Multi = 1
    for i in List:
        Multi = Multi * i

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   8/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [10,20,30,40]
    t1 = threading.Thread(target=Sum)
    t2 = threading.Thread(target=Multi)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(List)
    print("Sum is :",Sum)
    print("Multiplication is :",Multi)
   
if __name__ == "__main__":
    main()