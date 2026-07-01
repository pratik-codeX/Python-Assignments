'''
5. Write a program which accepts one number and 
checks whether it is palindrome or not.
Input: 121
Output: Palindrome
'''

#1  2   1  ==  1    2   1
def CheckPalindrome(No):
    Flag = False
    Digit = 0
    Rev = 0
    Cnt = 0
    while(No != 0):
        Digit = No % 10
        
        Cnt = Cnt +1 
        
        No = No // 10

def main():
    Flag = False
    Value = int(input("Enter Number :"))
    
    Flag = CheckPalindrome(Value)
    '''if(Flag == True):
        print("Its Palindrome Number")
    else:
        print("Its Not Palindrome Number ")'''

if __name__ == "__main__":
    main()