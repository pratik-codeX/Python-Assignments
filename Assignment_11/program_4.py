'''
4. Write a program which accepts one number and
 prints reverse of that number.
Input: 123
Output: 321
'''

def DisplayReverse(No):
    Digit = 0
    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No // 10

def main():
    Value = int(input("Enter Number :"))
    
    DisplayReverse(Value)

if __name__ == "__main__":
    main()