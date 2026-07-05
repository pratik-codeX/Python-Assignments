'''
7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
having length greater than 5.
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
    Arr = ["Pratik","Ramshashtri","Ravi"]

    Ret = list(filter(lambda Arr : (len(Arr) > 5),Arr))
    print(Ret)
    
if __name__ == "__main__":
    main()