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

def SquareSum(No):
    Sum = 0
    Result = []
    for i in range(1,No):
        Sum = Sum + i * i
        
    return Sum

def main():

    Arr = [1000000]

    aobj = multiprocessing.Pool()

    Result = aobj.map(SquareSum,Arr)

    print(Result)

if __name__ == "__main__":
    main()