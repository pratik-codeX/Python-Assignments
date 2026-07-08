'''
3: Design a Python application that creates two threads named EvenList and OddList.
•Both threads should accept a list of integers as input.
•The EvenList thread should:
◦Calculate and display their sum.
The OddList thread should:
◦Extract all odd elements from the list.
◦Calculate and display their sum.
Threads should run concurrently

'''
import threading

def EvenSum(Arr):
    lst = list()
    Sum = 0
    for i in Arr:
        if i % 2 == 0:
            lst.append(i)
            Sum = i + Sum
            
    print(Sum)
    print(lst) 

def OddSum(Arr):
    Sum = 0
    lst = list()
    for i in Arr:
        if i % 2 != 0:
            lst.append(i)
            Sum = i + Sum
            
    print(Sum)
    print(lst)


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    List = [2,3,4,5]

    EvenList = threading.Thread(target=EvenSum,args=(List,))
    OddList = threading.Thread(target=OddSum,args=(List,))
    
    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()