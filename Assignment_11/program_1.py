'''
1. Write a program which accepts one number and 
checks whether it is prime or not.
Input: 11
Output: Prime Number
'''

def CheckPrime(No):
    Flag = True
    for no in range(2,No):
        if(No % no == 0):
            Flag = False
            return Flag
        else:
            return Flag

def main():
    Flag = True
    Value = int(input("Enter Number :"))
    Flag = CheckPrime(Value)
    if(Flag):
        print(Value," is Prime Number")
    else:
        print(Value,"is not prime Number")
   
if __name__ == "__main__":
    main()