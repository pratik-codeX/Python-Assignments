'''
2.Write a program which accepts one number and 
prints count of digits in that number.
Input: 7521
Output: 4
'''

def CountDigit(No):
    Count = 0

    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    Value = int(input("Enter Number :"))
    
    ret = CountDigit(Value)

    print("Digits in ",Value,"are:",ret)

if __name__ == "__main__":
    main()