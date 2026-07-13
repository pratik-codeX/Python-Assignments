'''
1. Write a program that accepts a list of integers and uses Pool.map()
to calculate the sum of squares from 1 to N for every element in the
list.
Example Input
[1000000,2000000,3000000,4000000]
Expected Output
[333333833333500000,
2666668666667000000,
...
]
'''

import multiprocessing
import os

def SumEven(No):
    Sum = 0
    for i in range(No+1):
        if i % 2 == 0:
            Sum = i + Sum
        
    return Sum

def main():

    Arr = [1000000]

    aobj = multiprocessing.Pool()
    Result = aobj.map(SumEven,Arr)

    print("Process Id is :",os.getpid())
    print(Result)

if __name__ == "__main__":
    main()