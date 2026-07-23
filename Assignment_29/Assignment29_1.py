import os

def is_FileExists(FileName):
    ret = os.path.exists(FileName)

    if ret == False:
        print("File is not present")
    else:
        print("File Exists")

def main():

    is_FileExists("Demo.txt")

    FileName = input("Enter File Name :")

    try:
        fobj = open(FileName,"r")
        print("File Present")
    except FileNotFoundError as fobj:
        print("File Not Found in Current Folder")

if __name__ == "__main__":
    main()