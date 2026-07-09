import threading 

def PrimeList(Arr):
    lst = []
    for i in Arr:
        if i == 2:
            lst.append(i)

        for j in range(2,i+1//2):
            if i % j == 0:
               break
            else:
                lst.append(i)
                break

    print(lst)

def NonPrimeList(Arr):
    lst = []
    for i in Arr:
        for j in range(2,i+1//2):
            if i % j != 0 :
                break
            else:
                lst.append(i)
                break
                   
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

    Arr = [2,5,4,8,7]

    Prime = threading.Thread(target = PrimeList,args=(Arr,))
    NonPrime = threading.Thread(target=NonPrimeList,args=(Arr,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()
   

if __name__ == "__main__":
    main()