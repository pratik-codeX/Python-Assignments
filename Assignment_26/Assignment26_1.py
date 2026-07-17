'''
1: Write a Python program to implement a class named Demo with the following
specications:
•The class should contain two instance variables: no1 and no2.
•The class should contain one class variable named Value.
•De ne a constructor (__init__) that accepts two parameters and initializes the instance variables.
•Implement two instance methods:
◦Fun() – displays the values of instance variables no1 and no2.
◦Gun() – displays the values of instance variables no1 and no2.
Create two objects of the Demo class as follows:
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Call the instance methods in the given sequence:
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
'''

class Demo:
    value = 0

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print("Value of No1 form Fun is :",self.No1)
        print("Value of No2 from Fun is :",self.No2)


    def Gun(self):
        print("Value of No1 from Gun ;is :",self.No1)
        print("Value of No2 from Gun is :",self.No2)

def main():
    dobj1 = Demo(11,21)
    dobj2 = Demo(51,101)

    dobj1.Fun()
    dobj2.Fun()
    dobj1.Gun()
    dobj2.Gun()

if __name__ == "__main__":
    main()