'''
5. Write a program which accepts one number and 
checks whether it is palindrome or not.
Input: 121
Output: Palindrome
'''

def CheckPalindrome(No):
    Digit = 0
    Flag = False
    Num = 0
    while(No != 0):
        Digit = No % 10
        Num = Digit + 10                                                                                                                                                            
        No = No // 10

def main():
    Flag = False
    Value = int(input("Enter Number :"))
    
   Flag = CheckPalindrome(Value)

if __name__ == "__main__":
    main()