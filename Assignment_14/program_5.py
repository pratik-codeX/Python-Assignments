'''
5. Write a program which accepts marks and displays grade.
Condition Example:
≥ 60  First Class
≥ 50  Second Class
< 50  Fail
'''
    
def DisplayGrade(Marks):

    if(Marks >= 60):
        print("First Class")
    elif(Marks >= 50):
        print("Second Class")
    else:
        print("Fail")

def main():
    Marks = 0

    Marks = int(input("Enter Number :"))

    DisplayGrade(Marks)

if __name__ == "__main__":
    main()