'''
4: Write a program that creates a new log le after every ten minutes.
The lename should contain the current date and time.
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The le should contain:
Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
'''

import schedule
import datetime
import time
import os

def DirectoryScan(DirectoryName):
    SubCount = 0
    FileCount = 0
    TotalFile = 0
    log_file = open("DirectoryCountLog.txt","a")
    
    for DirectoryName1,SubDirectoryName,FileName in os.walk(DirectoryName):
        for Subdir in SubDirectoryName:
            log_file.write(DirectoryName+"/"+Subdir+"\n")
            for Fname in FileName:
                FileCount = FileCount + 1

    tobj = datetime.datetime.now()
    format_Time = tobj.strftime("%d-%m-%y %h:%m:%s %p")

    log_file.write("Total Files are : "+ str(FileCount) +"\n")
    log_file.write(format_Time+"\n")

def main():

    print("Automation Script Started...")

    schedule.every(1).seconds.do(DirectoryScan,"Hello")

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()