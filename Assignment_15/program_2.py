'''
2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even
numbers
'''

EvenNum = lambda Arr : Arr % 2 == 0

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Ret = 0
    Value = 0
    Arr = [11,22,51,100,122]

   
    Ret = list(filter(EvenNum,Arr))

    print(Ret)
   
if __name__ == "__main__":
    main()