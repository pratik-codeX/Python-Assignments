'''
4. Write a program which accepts one number and prints cube of that number.
'''

def CubeX(No1):
    if(No1 <= 0):
        print("Enter Valid Number")
        return
    return No1 * No1 * No1

def main():
    Value1 = int(input("Enter Number :"))
    
    ret = CubeX(Value1)

    print("Cube is :",ret)

if __name__ == "__main__":
    main()