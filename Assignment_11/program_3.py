'''
3. Write a program which accepts one number and prints sum of digits.
Input: 123
Output: 6
'''

def SumofDigit(No):
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter Number :"))
    
    ret = SumofDigit(Value)

    print("Sum of digit is :",ret)

if __name__ == "__main__":
    main()