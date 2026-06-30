'''
2. Write a program which contains one function ChkGreater() 
    that accepts two numbers
    and prints the greater number.

Input: 10 20
Output: 20 is greater
'''

def ChkGreater(No1,No2):
    if(No1 < No2):
        return No2
    else:
        return No1

def main():
    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))
    
    ret = ChkGreater(Value1,Value2)

    print(ret,"is Greater")

if __name__ == "__main__":
    main()