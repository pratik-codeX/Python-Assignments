'''
3: Write a Python program to implement a class named Numbers with the following
speci cations:
•
The class should contain one instance variable:
◦
•De ne a constructor (__init__) that accepts a number from the user and initializes Value.
•Implement the following instance methods:
◦ChkPrime() – returns True if the number is prime, otherwise returns False
◦ChkPerfect() – returns True if the number is perfect, otherwise returns False
◦Factors() – displays all factors of the number
◦SumFactors() – returns the sum of all factors
Create multiple objects and call all methods.
'''

class Numbers:
    def __init__(self,No):
        self.No = No

    def ChkPrime(self):
        Flag = True
        for i in range(2,self.No//2):
            if self.No % i == 0:
                Flag = False

        return Flag
    
    def ChkPerfect(self):
        Perfect = 0
        Flag = False
        for i in range(1,self.No):
            if self.No % i == 0:
                Perfect = Perfect + i

        if Perfect == self.No:
            Flag = True

        return Flag   

    def Factors(self):
        for i in range(1,self.No+1//2):
            if self.No % i == 0:
                print(f"Factors of {self.No} are : \t {i} \t")
    
    def SumFactors(self):
        Sum = 0
        for i in range(1,self.No+1//2):
            if self.No % i == 0:
                Sum = Sum + i
        
        return Sum

def main():
    nobj = Numbers(8)

    nobj.ChkPrime()
    nobj.ChkPerfect()
    nobj.Factors()
    print(f"Sum of Factors is : {nobj.SumFactors()}")

if __name__ == "__main__":
    main()