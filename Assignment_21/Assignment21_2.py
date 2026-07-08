import threading

def EvenFactorsSummation(No):
    FactSum = 0
    for i in range(2,No):
        if No % i == 0 and i % 2 == 0:
            FactSum = i + FactSum

    print(FactSum)

def OddFactorsSummation(No):
    FactSum = 0
    for i in range(2,No):
        if No % i == 0 and i % 2 != 0:
            FactSum = i + FactSum

    print(FactSum)


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Value = int(input("Enter Number :"))

    EvenFactor = threading.Thread(target=EvenFactorsSummation,args=(Value,))
    OddFactor = threading.Thread(target=OddFactorsSummation,args=(Value,))
    
    EvenFactor.start()
    EvenFactor.join()

    OddFactor.start()
    OddFactor.join()


if __name__ == "__main__":
    main()
    print("Exit from main")