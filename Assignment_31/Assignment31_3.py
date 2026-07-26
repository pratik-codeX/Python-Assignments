import schedule
import datetime
import time
import os

def DirectoryScan(DirectoryName):
    SubCount = 0
    FileCount = 0
    TotalFile = 0
    for DirectoryName,SubDirectoryName,FileName in os.walk(DirectoryName):
        for SubDir in SubDirectoryName:
            SubCount = SubCount + 1
            print("Inside Subdir :",SubDir)
        for Fname in FileName:
            FileCount = FileCount + 1

    TotalFile = SubCount + FileCount
    tobj = datetime.datetime.now()

    format_Time = tobj.strftime("%d-%m-%y %I:%M:%S %p")

    print("Directory Scanned : ",DirectoryName)
    print("Total Files :",TotalFile)
    print("Total Subdirectories : ",SubCount)
    print("Scan Time : ",format_Time)

def main():

    DirectoryName = input("Enter Directory Name :")

    print("Automation Script Started...")

    schedule.every(1).minutes.do(DirectoryScan, DirectoryName)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()