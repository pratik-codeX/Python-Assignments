'''
8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
divisible by both 3 and 5.
'''

DivisibleDigit3and5 = lambda Arr:Arr%5 == 0 and Arr % 3 == 0


def main():
    Arr = [13,15,5,12,30]

    Ret = list(filter(DivisibleDigit3and5,Arr))
    
    print(Ret)
if __name__ == "__main__":
    main()