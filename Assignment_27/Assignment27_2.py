'''
2: Write a Python program to implement a class named BankAccount with the following
requirements:
•
•
The class should contain two instance variables:
◦Name (Account holder name)
◦Amount (Account balance)
The class should contain one class variable:
◦
•De ne a constructor (__init__) that accepts Name and initial Amount.
•Implement the following instance methods:
Display() – displays account holder name and current balance
'''

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Balance):
        self.Name = Name
        self.Balance = Balance

    def Display(self):
        print(f"Account Holder Name is :{self.Name}")
        print(f"Account Balance is :{self.Balance}")

    def Deposit(self):
        Amount = int(input("Enter Amound for Deposit :"))
        self.Balance = self.Balance + Amount

    def Withdraw(self):
        Amount = int(input("Enter Amount for Withdraw : "))
        if Amount > self.Balance:
            print(f"Insufficient Balace Enter Less Amount than :{self.Balance}")
            self.Withdraw()
        if Amount < 0 :
            print("Amount Can't be negative")
            self.Withdraw()

        self.Balance = self.Balance - Amount
        return self.Balance - Amount

    def CalculateInterest(self):
        Amount = int(input("Enter Amount for Interest :"))
        Interest = (Amount * BankAccount.ROI) /100

        return Interest

def main():
    
    bobj = BankAccount("Pratik Raut",100000)

    bobj.Display()

    print(f"Interest on Amount is :{bobj.CalculateInterest()}")

if __name__ == "__main__":
    main()