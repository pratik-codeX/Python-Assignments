'''
1.What is the difference between List and Tuple in Python?
Explain in terms of:
•Mutability
•Memory
•Performance
•Use cases

    10,20,5,40
'''

def Iteration_List(list):
    for i in range(len(list)):
        print(list[i])
    
    
def Find_Min(list):
        min = list[0]
        for i in range(len(list)):
            if(list[i] < min):
                min = list[i]
        
        return min
        


def Iteration_Tuple(tuple):
    for i in range(len(tuple)):
        print(tuple[i])

def main():
    list = [10,20,5,30]
    #print(list)
    #print(type(list))
    #print(id(list))
    tuple = (10,20,30)

    tuple[0] = 100
    #print(tuple)
    #print(type(tuple))
    #print(id(tuple))

    Iteration_List(list)
    ret = Find_Min(list)
    print("Minimum number in list is : ",ret)
    print("-----------------------")
    #Iteration_Tuple(tuple)


if __name__ == "__main__":
    main()