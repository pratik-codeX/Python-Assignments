'''
3. Write a program which accepts one number and prints square of that number.
Input: 5
Output: 25
'''

def SquareX(No1):
    if(No1 <= 0):
        print("Enter Valid Number")
        return
    return No1 * No1

def main():
    Value1 = int(input("Enter Number :"))
    
    ret = SquareX(Value1)

    print("Square is :",ret)

if __name__ == "__main__":
    main()