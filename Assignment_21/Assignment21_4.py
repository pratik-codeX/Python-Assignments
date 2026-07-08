'''
4: Design a Python application that creates three threads named Small, Capital, and
Digits.
•All threads should accept a string as input.
•The Small thread should count and display the number of lowercase characters.
•The Capital thread should count and display the number of uppercase characters.
•The Digits thread should count and display the number of numeric digits.
•Each thread must also display:
◦Thread ID
◦Thread Name
'''

import threading

def lowerCase(Arr):
    Lst = []
    Count = 0
    for i in Arr:
        if i > 'a' and i < 'z':
            Lst.append(i)
            Count =1 + Count
    
    print(Lst)
    print(Count)
    print("Thread id :",threading.get_ident())

def upperCase(Arr):
    Lst = []
    Count = 0
    for i in Arr:
        if i >= 'A' and i <= 'Z':
            Lst.append(i)
            Count =  1 + Count
    
    print(Lst)
    print(Count)


def CountDigit(Arr):
    Lst = []
    Count = 0

    for i in Arr:
        if i >= '0' and i <= '9':
            Lst.append(i)
            Count = 1 + Count
    
    print(Lst)
    print(Count)


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   8/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Str = "1PraTik2"

    Small = threading.Thread(target=lowerCase,args=(Str,))
    Capital = threading.Thread(target=upperCase,args=(Str,))
    Digit = threading.Thread(target=CountDigit,args=(Str,))

    Small.start()
    Capital.start()
    Digit.start()

    Small.get_ident()

    Small.join()
    Capital.join()
    Digit.join()
   
if __name__ == "__main__":
    main()