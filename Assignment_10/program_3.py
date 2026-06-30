'''
3. Write a program which accepts one number and prints 
factorial of that number.
Input: 5
Output: 120
'''

def Factorial(No):
    Fact = 1
    if(No <= 0):
        print("Enter Valid Number")
        return
    
    for i in range(1,No+1):
        print(i)
        Fact = Fact * i
    return Fact 

def main():
    Value = int(input("Enter Number :"))
    
    ret = Factorial(Value)

    print("Factorial of",Value," is",ret)

if __name__ == "__main__":
    main()