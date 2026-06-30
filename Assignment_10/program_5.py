'''
5.Write a program which accepts one number and 
prints all odd numbers till that number.
'''

def DisplayOdd(No):
    for no in range(1,No+1):
        if(no % 2 != 0):
            print(no)

def main():
    Value= int(input("Enter Number :"))
    
    DisplayOdd(Value)

if __name__ == "__main__":
    main()