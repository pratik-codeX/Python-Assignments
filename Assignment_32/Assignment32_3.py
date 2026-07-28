import schedule
import datetime
import time
import os

def DirectoryScan(DirectoryName,Filename):
    for DirectoryName,SubDirectoryName,FileName in os.walk(DirectoryName):
        for Fname in FileName:
            if Filename == Fname:
                fname = os.path.join(DirectoryName,Fname)

    return fname

def DisplayContent(DirectoryName,Filename):

    ret = True

    Fname = DirectoryScan(DirectoryName,Filename)

    if ret == os.path.exists(Fname) and ret == os.path.isfile(Fname) == False:
        print("File Does not Exists")
        return 

    try:
        fobj = open(Fname,"r")
        ret = fobj.seek(0,2)
        if ret == 0:
            print("File is empty")

        fobj.seek(0)
        print(fobj.read())

        print("Size of file is :",fobj.tell())

    except Exception as eobj:
        print(eobj)

def main():

    DirectoryName = input("Enter Directory Name :")
    Filename = input("Enter File Name :")
    
    print("Automation Script Started...")

    schedule.every(1).minutes.do(DisplayContent,DirectoryName,Filename)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()