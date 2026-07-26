'''
Q4) Compare Two Files (Command Line)
If both les contain the same contents, display Success
•Otherwise display Failure
Input (Command Line):
Demo.txt Hello.txt
Expected Output:
Success OR Failure
'''
import sys
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():

    try:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Run Application as : python Filename.py File1.txt File2.txt")
            return
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]
        fobj1 = open(FileName1,"r")
        fobj2 = open(FileName2,"r")
  
    except IndexError as iobj:
        print("Enter Command Line Argument")
        print("Enter : --h for help")
        return
    except FileNotFoundError as fobj:
        print("File Not Found in Current Folder")
    except Exception as eobj:
        print("Error :",eobj)

    ret1 = CalculateChecksum(FileName1)
    ret2 = CalculateChecksum(FileName2)

        
    if ret1 == ret2:
        print("Content Inside files are same")
    else:
        print("Content Inside files are not same")

if __name__ == "__main__":
    main()