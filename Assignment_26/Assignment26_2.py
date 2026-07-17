class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
        self.Radius = int(input("Enter Radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius*self.Radius)
        return self.Area
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        return self.Circumference
    
    def Display(self):
       print(f"Area of {self.Radius} is : ",self.CalculateArea())
       print(f"Circumference of {self.Radius} is : ",self.CalculateCircumference())
       print("\n")

    
def main():
    cobj1 = Circle()
    cobj2 = Circle()
    cobj3 = Circle()
    
    cobj1.Accept()
    cobj1.Display()

    cobj2.Accept()
    cobj2.Display()

    cobj3.Accept()
    cobj3.Display()

if __name__ == "__main__":
    main()
    
