'''
5. Write a program which accepts one number and checks 
    whether it is divisible by 3 and 5
Input: 15
Output: Divisible by 3 and 5
'''

def CheckDivisible(No1):
    if((No1 % 3 == 0) and (No1 % 5 == 0)):
        return True
    else:
        return False

def main():
    Value1 = int(input("Enter Number :"))
    
    ret = CheckDivisible(Value1)
    if(ret):
        print(Value1," is Divisible by 3 and 5")
    else:
        print(Value1,"is not Divisible by 3 and 5")





if __name__ == "__main__":
    main()