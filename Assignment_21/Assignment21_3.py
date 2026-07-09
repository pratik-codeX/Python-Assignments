'''
3: Design a Python application where multiple threads update a shared variable.
•Use a Lock to avoid race conditions.
•Each thread should increment the shared counter multiple times.
•Display the nal value of the counter after all threads complete execution.

'''
import threading

thread_lock = threading.Lock()
Cnt = 0

def Counter():
    global Cnt
    
    for i in range(100):
        
        thread_lock.acquire()
        
        Cnt = Cnt + 1               #Critical Section

        thread_lock.release()


###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():

    print("Inside Main")

    t1 = threading.Thread(target=Counter)
    t2 = threading.Thread(target=Counter)
    t3 = threading.Thread(target=Counter)
    t4 = threading.Thread(target=Counter)
    t5 = threading.Thread(target=Counter)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print(Cnt)

    print("End of main")

if __name__ == "__main__":
    main()