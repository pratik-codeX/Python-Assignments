'''
3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
numbers.
'''

OddNum = lambda Arr : Arr % 2 != 0
      
###########################################################################
##  Function Name  	:  main
##  Description    	:  Client 
##  Input          	:  
##	Output         	: 
##	Date           	:   1/7/2026
##  Author  		:   Pratik Raut
###########################################################################

def main():
    Arr = [11,21,50,101,121]

    Ret = list(filter(OddNum,Arr))
    print(Ret)

if __name__ == "__main__":
    main()
