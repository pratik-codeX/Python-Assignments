'''
2. Write a program which accepts one number and prints
     sum of first N natural numbers.
Input: 5
Output: 15
'''

def NNaturalNumber(No):
    Sum = 0
    for no in range(1,No+1,1):
        Sum = no + Sum

    return Sum

def main():
    Value = int(input("Enter Number :"))
    
    ret = NNaturalNumber(Value)

    print(ret)

if __name__ == "__main__":
    main()