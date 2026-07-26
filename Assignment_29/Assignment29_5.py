'''
Q5) Frequency of a String in File
Problem Statement:
Write a program which accepts a le name and one string from the user and returns the frequency (count of
occurrences) of that string in the le.
Input:
Demo.txt Marvellous
Expected Output:
Count how many times "Marvellous" appears in Demo.txt
'''

import sys

def WordOccurance(FileName,word):
    fobj = open(FileName,"r")

    ptr = fobj.seek(0,2)

    fobj.seek(0)
    str = ""

    while(ptr > 0):
        Buffer = fobj.read(1000)

        for i in Buffer:
            str = str + i
            if i == " ":
                print(str == word)
                break

        prt = ptr -1


def main():

    try:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Run Application as : python Filename.py File1.txt File2.txt")
            return
        FileName = sys.argv[1]
        Word = sys.argv[2]
        fobj = open(FileName,"r")
          
    except IndexError as iobj:
        print("Enter Command Line Argument")
        print("Enter : --h for help")
        return
    except FileNotFoundError as fobj:
        print("File Not Found in Current Folder")
    except Exception as eobj:
        print("Error :",eobj)

    WordOccurance(FileName,Word)

    

if __name__ == "__main__":
    main()
