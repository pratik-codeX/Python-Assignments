'''
2: Write a Python program that monitors the size of a specifcied file
every 30 seconds.
Write the following details into:
FileSizeLog.txt
•File path
•File size in bytes
•Date and time
Handle the situation where the file does not exist.
'''

import schedule
import datetime
import time
import os


def checkfile_exists(FilePath,FileName):
    Flag = False
    ret = os.path.isdir(FilePath)
    if ret == False:
        print("Invalid Input its Not Directory")
        return

    for DirName,SubDir,filename in os.walk(FilePath):
        for fname in filename:
            if fname == FileName:
                fnme = os.path.join(DirName,fname)
                Flag = True

    if Flag == False:
        print("File not Found")
        return FileNotFoundError
    else:
        return fnme
                        
def monitor_file(FilePath,Filename):

    fname = checkfile_exists(FilePath,Filename)

    try:
        fobj = open(fname,"a")
    except Exception as eobj:
        print("File not Found")
        return

    fobj = open(fname,"a")

    dobj = datetime.datetime.now()
    ptr = fobj.seek(0,2)

    date_time = dobj.strftime("%d-%m-%Y and %I:%M")

    log = open("FileSizeLog.txt","a")

    log.write(f"File Name is :{fname} and Size of File is : {ptr} \n Date and Time : {date_time}\n\n")

def main():

    FilePath = input("Enter path : ")
    Fname = input("Enter File Name :")

    monitor_file(FilePath,Fname)
                
    print("Automation Script Started...")

    schedule.every(5).seconds.do(monitor_file,FilePath,Fname)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()