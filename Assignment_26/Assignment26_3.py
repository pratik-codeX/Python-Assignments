'''
Write a Python program to implement a class named Arithmetic with the following
characteristics:

•The class should contain two instance variables: Value1 and Value2.
•De ne a constructor (__init__) that initializes all instance variables to 0.
•Implement the following instance methods:
◦Accept() – accepts values for Value1 and Value2 from the user.
◦Addition() – returns the addition of Value1 and Value2.
◦Subtraction() – returns the subtraction of Value1 and Value2.
◦Multiplication() – returns the multiplication of Value1 and Value2.
◦Division() – returns the division of Value1 and Value2 (handle division by zero
properly).
Create multiple objects of the Arithmetic class and invoke all the instance methods.
'''

class Arithmetic:

    def __init__(self):
        self.No1 = 0
        self.No2 = 0

    def Accept(self):
        self.No1 = int(input("Enter First Number :"))
        self.No2 = int(input("Enter Second Number :"))
    
    def Addition(self):
        return self.No1 + self.No2

    def Substration(self):
        return self.No1 - self.No2
    
    def Multiplication(self):
        return self.No1 * self.No2
    
    def Division(self):
        
        try:
            return self.No1 // self.No2
        
        except ZeroDivisionError as Zobj:
           print("Divisor can not be Zero as Exception is :",Zobj)

def main():
    
    Aobj = Arithmetic()

    Aobj.Accept()

    print("Addition is :",Aobj.Addition())
    print("Substraction is :",Aobj.Substration())
    print("Multiplication is :",Aobj.Multiplication())
    print("Division is :",Aobj.Division())

if __name__ == "__main__":
    main()
    
