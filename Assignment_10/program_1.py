'''
1. Write a program which accepts one number and
     prints multiplication table of that number.

Input: 4
Output:  4 8 12 16 20 24 28 32 36 40
'''

def DisplayTable(No):
    for no in range(No,No*11,No):
        print(no)

def ShowTable(No):
    Count = 1
    temp = 0
    while(Count < 11):
        temp = No * Count
        Count = Count +1
        print(No)

def ShowTableList(No):
    lst = list()
    for no in range(No,No*11,No):
        lst.append(no)
        
    return lst

def main():
    Value = int(input("Enter Number :"))
    Arr = []
    #DisplayTable(Value)
    Arr = ShowTableList(Value)
    print(Arr)

    #ShowTable(Value)

if __name__ == "__main__":
    main()