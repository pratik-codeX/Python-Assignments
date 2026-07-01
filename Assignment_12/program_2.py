'''
2. Write a program which accepts one number and prints its factors.
Input: 12
Output: 1 2 3 4 6 12
'''

def DisplayFactors(No):
    Count = 0

    for i in range(1,No+1,1):
        if(i % 2 == 0):
            print(i)

def main():
    Value = int(input("Enter Number :"))
    
    DisplayFactors(Value)

if __name__ == "__main__":
    main()