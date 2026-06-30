'''
4. Write a program which accepts one number and 
prints all even numbers till that
number.
Input: 10
Output: 2 4 6 8 10
'''

def DisplayEven(No):
    for no in range(1,No+1):
        if(no % 2 == 0):
            print(no)

def main():
    Value = int(input("Enter Number :"))
    
    DisplayEven(Value)

if __name__ == "__main__":
    main()