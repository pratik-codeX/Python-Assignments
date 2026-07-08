'''
1: Design a Python application that creates two separate threads named Even and Odd.
•The Even thread should display the first 10 even numbers.
•The Odd thread should display the first 10 odd numbers.
•Both threads should execute independently using the threading module.
•Ensure proper thread creation and execution.
'''


import threading 

def DisplayEven(No):
    print(30*"*")
    for i in range(0,No):
        print(i*2)

def DisplayOdd(No):
    print(30*"*")
    for i in range(No):
        print(i*2+1)

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():

    Even = threading.Thread(target = DisplayEven,args=(10,))
    Odd = threading.Thread(target=DisplayOdd,args=(10,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
   
if __name__ == "__main__":
    main()