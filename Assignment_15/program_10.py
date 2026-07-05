'''
10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
numbers.
'''

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


def main():
    Arr = [10,2,30,5,7,1]

    Ret = list(filter(lambda Arr : (Arr % 2 == 0),Arr))
    print(len(Ret))
    
if __name__ == "__main__":
    main()