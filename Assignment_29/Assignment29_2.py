import os

def main():
    
    FileName = input("Enter File Name :")

    try:
        fobj = open(FileName,"r")
        print("File Present")
    except FileNotFoundError as fobj:
        print("File Not Found in Current Folder")

    print(fobj.read())

if __name__ == "__main__":
    main()