'''
3. Write a program which accepts two numbers and prints addition, subtraction,
multiplication and division.
'''

Addiiton = lambda No1 , No2 :  No1 + No2 
Substration = lambda No1 , No2 :  No1 - No2 
Multiplication = lambda No1 , No2 :  No1 * No2 
Division = lambda No1 , No2 :  No1 // No2 

def main():
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))

    Ret1 = Addiiton(Value1,Value2)
    Ret2 = Substration(Value1,Value2)
    Ret3 = Multiplication(Value1,Value2)
    Ret4 = Division(Value1,Value2)

    print("Addition is :",Ret1)
    print("Substration is :",Ret2)
    print("Multiplication is :",Ret3)
    print("Division is :",Ret4)
    
if __name__ == "__main__":
    main()