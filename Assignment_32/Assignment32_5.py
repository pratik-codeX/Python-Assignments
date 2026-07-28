'''
5: Write a program that deletes all empty files from a specified
directory every hour.
The program should:
•Scan the directory recursively
•Detect files whose size is zero bytes
•Delete the empty files
•Store deleted file paths in a log file
•Handle permission errors
Test the program only on a sample directory.
'''

import os 
import time
from pathlib import Path
import schedule


def DirectoryTraversal(DirName):

    if os.path.exists(DirName) == False:
        print("Directory Does not Exists\n")
        return
    
    if os.path.isdir(DirName) == False:
        print("Its not Directory\n")
        return

    for Dir,Sub,File in os.walk(DirName):
        for file in File:
            file = os.path.join(Dir,file)
            DeleteEmptyFile(file)

def DeleteEmptyFile(FileName):

    fobj = open(FileName,"r")
    log = open("DeletedLog.txt","a+")

    ptr = fobj.seek(0,2)

    if ptr == 0:
        os.remove(FileName)
        log.write(f"Deleted Files are : {FileName}")
        
def main():

    Directory = input("Directory Path is : ")
    print("Automation Started")

    schedule.every(1).hour.do(DirectoryTraversal,Directory)


    while(True):

        schedule.run_pending()

        time.sleep(1)

    print("Automation Ended")

if __name__ == "__main__":
    main()

