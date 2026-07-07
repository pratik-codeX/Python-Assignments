from MarvellousNum import ChkPrime

def ListPrime(lst):
    result = 0
    Size = int(input("Enter Number of elements : "))
    print("*"*50)
    print("Input Elements :")

    for i in range(Size):
        result = int(input(f"Element Number {i} :"))
        lst.append(result)
    
    return lst

def main():
    Arr = list()
    LRet = list()

    LRet = ListPrime(Arr)

    Result,Sum = ChkPrime(LRet)

    print(Result,Sum)

    
if __name__ == "__main__":
    main()